package Kasetsu::Infrastructure::TextDatabase::FileLock;
use strict;
use warnings;
use utf8;

sub save_data {
  # $datadir = $CHARA_DATA | $LOG_DIR
  my ($filename, $data, $datadir) = @_;

  my $tmp_filename       = $filename . '.tmp';
  my $tmp_dummy_filename = $filename . '.dmy.tmp';
  my $file               = substr($filename, length($datadir) + 1);

  opendir(my $dh, $datadir);
  my @filenames = readdir $dh;
  closedir $dh;

  for my $filename (@filenames) {
    if ($filename =~ /($file).*\.tmp$/) {
      my $mtime   = (stat $tmp_filename)[9];
      my $at_last = time - 60 - $mtime;
      unlock() if $mtime && 0 < $at_last;
      die "テンポラリファイルが存在します。ロック解除まで $at_last 秒";
    }
  }

  eval {
    open my $tmp, '>', $tmp_filename or die "テンポラリファイルが作成出来ません。($!)";
    $tmp->close or die "テンポラリファイルがクローズ出来ません。($!)";

    open my $dummy, '>', $tmp_dummy_filename or die "格納用一時ファイルが作成出来ません。($!)";
    $dummy->close or die '';

    chmod 0666, $tmp_dummy_filename or die $!;

  };
  unlock() if $@;

  open my $dummy, '>', $tmp_dummy_filename or die "格納用一時ファイルがオープン出来ません。($!)";
  $dummy->print(@$data);
  $dummy->close or die $!;

  rename $tmp_dummy_filename, $filename or die $!;
  unlink $tmp_filename or die $!;
}

sub unlock {
  my ($tmp_filename, $tmp_dummy_filename) = @_;
  unlink $_ for ($tmp_filename, $tmp_dummy_filename);
}

1;
