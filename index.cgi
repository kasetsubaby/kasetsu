#!/usr/bin/env perl

#################################################################
#   �y�Ɛӎ����z                                                #
#    ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B         #
#    �܂��ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B       #
#################################################################

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.pl';
require 'check_com.cgi';

if($MENTE) { &ERR2("�X�N���v�g�`�F�b�N�̈׈ꎞ�I�ɒ�~���܂��B"); }
&DECODE;
&INDEX;

#_/_/_/_/_/_/_/_/_/#
#_/  INDEX���   _/#
#_/_/_/_/_/_/_/_/_/#

sub INDEX {

	$date = time();
	$month_read = "$LOG_DIR/date_count.cgi";
	open(IN,"$month_read") or &ERR2("Can\'t file open!:month_read");
	@MONTH_DATA = <IN>;
	close(IN);
	&TIME_DATA;

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=008800>��</font>$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$D_MES .= "<font color=000088>��</font>$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$old_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "$LOG_DIR/act_log.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>��</font>$ACT_DATA[$p]<BR>";$p++;}
		$ACT_MES = "<TR><TD bgcolor=#EFE0C0 colspan=\"2\" width=80% height=20><font color=#8E4C28 size=2>$A_MES</font></TD></TR>";

	}

	open(IN,"$TOWN_LIST") or &ERR2('Can\'t file open!:month_read:TOWN_LIST');
	@TOWN_DATA = <IN>;
	close(IN);
	($zwname,$wzc)=split(/<>/,$TOWN_DATA[0]);
	$zzhit=0;
	foreach(@TOWN_DATA){
		($zwname,$zwcon)=split(/<>/);
		if($wzc ne $zwcon){$zzhit=1;}
		$wzc = $zwcon;
	}

	# PLAYER DATA UPDATE
	&CHECK_COM;

	# MASTER DATA UPDATE
	if($mtime + $TIME_REMAKE < $date){
		if($mtime eq ""){
			$mtime = $date;
			&MAP_LOG("�Q�[���v���O�������J�n���܂����B");
		}else{
			$mtime += $TIME_REMAKE;
		}
		$mmonth++;
		if($mmonth > 12){
			$myear++;
			$mmonth=1;
		}
		unshift(@month_new,"$myear<>$mmonth<>$mtime<>\n");
		if($ACT_LOG){
			($qsec,$qmin,$qhour,$qday) = localtime($mtime);
			unshift(@ACT_DATA,"===============\[$myear�N$mmonth��\]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('�t�@�C�����J���܂���ł����Berr no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY �f�[�^���������߂܂���B');
		print OUT @NEW_COU_DATA;
		close(OUT);

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("$mmonth��:<font color=orange>�ŋ�</font>�Ŋe�����ɋ��^���x�����܂����B");
			$b_hit = 1;
		}elsif($mmonth eq "7"){
			&MAP_LOG("$mmonth��:<font color=orange>���n</font>�Ŋe�����ɕĂ��x�����܂����B");
			$b_hit = 1;
		}

		# EVENT ACTION
		$eve_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);
		$ihit=0;
		if(!int(rand(40))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���Ȃ��̑�Q�������P���܂����I");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���Ȃ��̑�Q�������P���܂����I");
			}elsif($ino eq 1){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�^����������܂����I�e�n�Ŕ�Q���o�Ă��܂��I");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�^����������܂����I�e�n�Ŕ�Q���o�Ă��܂��I");
			}elsif($ino eq 2){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�u�a�����s���Ă���悤�ł��B�X�̐l�X���ꂵ��ł��܂��B�B");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�u�a�����s���Ă���悤�ł��B�X�̐l�X���ꂵ��ł��܂��B�B");
			}elsif($ino eq 3){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���N�͖L��ɂȂ肻���ł��B");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]���N�͖L��ɂȂ肻���ł��B");
			}elsif($ino eq 4){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]��n�k��������܂����I");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]��n�k��������܂����I");
			}elsif($ino eq 5){
				&MAP_LOG("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�e���̏��X��������Ă��܂��B");
				&MAP_LOG2("<font color=red>�y�C�x���g�z</font>\[$eve_date\]�e���̏��X��������Ă��܂��B");
			}
		}
		if($b_hit){
			@NEW_TOWN_DATA=();
			foreach(@TOWN_DATA){
				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/);
				# ����ϓ�
				if(!int(rand(2.0))){
					$zsouba += int(rand(0.5)*100)/100;
					if($zsouba > 1.2){
						$zsouba = 1.2;
					}
				}else{
					$zsouba -= int(rand(0.5)*100)/100;
					if($zsouba < 0.8){
						$zsouba = 0.8;
					}
				}
				if($zpri >= 50){
					$znum_add = int(80 * ($zpri - 50));
					if($znum_add < 500){$znum_add=500;}
					$znum += $znum_add;
					if($znum > $NOU_MAX){$znum=$NOU_MAX;}
				}else{
					$znum -= int(80 * (50 - $zpri));
					if($znum < 0){$znum=0;}
				}
				# EVENT
				if($ihit){
					if($ino eq 0){
						$znou = int($znou * 0.8);
					}elsif($ino eq 1){
						$znou = int($znou * 0.9);
						$zsyo = int($zsyo * 0.9);
						$zshiro = int($zshiro * 0.9);
					}elsif($ino eq 2){
						$znum = int($znum * 0.8);
					}elsif($ino eq 3){
						$znou = int($znou * 1.2);
						if($znou > $znou_max){$znou=$znou_max;}
					}elsif($ino eq 4){
						$znou = int($znou * 0.8);
						$zsyo = int($zsyo * 0.8);
						$zshiro = int($zshiro * 0.8);
						$znum = int($znum * 0.9);
					}elsif($ino eq 5){
						$zsyo = int($zsyo * 1.1);
						if($zsyo > $zsyo_max){$zsyo=$zsyo_max;}
						$znum = int($znum * 1.1);
						if($znum > $NOU_MAX){$znum=$NOU_MAX;}
					}
				}
				push(@NEW_TOWN_DATA,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
			}
			&SAVE_DATA($TOWN_LIST,@NEW_TOWN_DATA);
		}
		&SAVE_DATA($month_read,@month_new);
	}
	if($ACT_LOG){
		if(@ACT_DATA > 800) { splice(@ACT_DATA,800); }
		open(OUT,">$actfile");
		print OUT @ACT_DATA;
		close(OUT);
	}

	$MESS1 = "<A href=\"$FILE_CONTNUE\">�yCONTNUE�z</a>";
	$MESS2 = "<A href=\"$FILE_ENTRY\">�y�V�K�o�^�z</a>";
	&COUNTER;
	$new_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);

	&HEADER;
	print <<"EOM";
<br>
<center>
  <table width="100%" height=100% cellpadding="0" cellspacing="0" border=0>
    <tr>
      <td align=center>
        <table border=0 width=80% height=100% cellspacing=1>
          <tbody>
            <tr>
              <td align=center>
                <p>
                  <table width=80% height=140 bgcolor=#DECCA8>
                    <tr>
                      <td align=center bgcolor=#EFE0C0>
                        <h1><div style="position:relative;"><s><font color=442200>$GAME_TITLE</font></s></div><div style="margin-bottom:-40px;padding:10px;border:1px solid #999;display:inline-block;position:relative;top:-40px;left:-100px;background:#fff;font-size:12px;transform:rotate(-15deg);">���݂̎O���uNET</div></h1>
                        <p><font size=2 color=#9c5a4b></font></p>
                        <p><font size=2 color=#9c5a4b><b>[$new_date]</b><br>
                          ����̍X�V�܂� <b>$next_time</b> ��<br>
                          <table bgcolor="#fff">
                            <tbody>
                              <tr>
                                <td>
                                  <font size="2">�V�K�o�^�i�����j�͂�����I��</font><a href="entry.cgi"><b><font size="4">�y���V�K�o�^���z</font></b></a><br>
                                  <a href="http://www35.atwiki.jp/densetu0net/pages/65.html" target="_blank">�`���̎O���uNETwiki-���S�Ҏw��</a><br>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </font></p>
                      </td>
                      <td align="center" bgcolor="#EFE0C0">
                        [<s>�g�їp</s>]<br><br><br><br>
                      </td>
                    </tr>
                  </table>
                </p>
                <p align="center">
                  <table>
                    <tbody>
                      <tr>
                        <td>
                          <table bgcolor="#842" border="0">
                            <tbody>
                              <tr>
                                <td bgcolor="#EFE0C0">
                                  <b>���Q�[���ڍ�</b>
                                </td>
                              </tr>
                              <tr>
                                <td bgcolor="#EFE0C0">
                                  <s>�yHOME(�`��.NET)�z</s><br><br>
                                  <a href="entry.cgi">�y�V�K�o�^�z</a> <br><br>
                                  <a href="ranking.cgi" target="_blank">�y�o�^�����ꗗ�z</a><br> <br>
                                  <a href="manual.html" target="_blank">�y�������z</a> <br><br>
                                  <a href="./map.cgi" target="_blank">�y���͐}�z</a><br><br>
                                  <a href="./ranking2.cgi" target="_blank">�y�����ꗗ�z</a><br><br>
                                  <a href="ranking5.cgi" target="_blank">�y���v���z</a><br><br>
                                  <s>�y�j�L�z</s> <br><br>
                                  <a href="https://jbbs.shitaraba.net/bbs/subject.cgi/netgame/16486/" target="_blank">��p�a�a�r</a><br><br>
                                  <a href="http://www35.atwiki.jp/densetu0net/" target="_blank">�`���Iwiki</a><br><br>
                                  <s>�O���uNET�����L���O</s><br><br>
                                  <s>�����u���E�U�Q�[��</s><br>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                        <td>
                          <table bgcolor="#842" border="0">
                            <tbody>
                              <tr>
                                <td bgcolor="#EFE0C0">
                                  <b>�����m�点���X�V����</b>
                                </td>
                              </tr>
                              <tr>
                                <td bgcolor="#EFE0C0">
                                  <b>/*�Q�O�P�S�N*/</b><br>
                                  <font size="2">�T/�Q�R�F<s>�����̉����ɂ���</s>�B������Ȋ����Ői�߂Ă������Ǝv���܂��B<br>
                                  </font><br><br>
                                  <font size="3" color="red">�V/�V�F����œ�����Z�\�̏ڍׂ��܂Ƃ߂Ă݂܂����B�x���Ȃ��Đ\����Ȃ��ł����B�� <s>���������Z�\�̈ꗗ��</s></font><br><br>
                                  <b>/*�Q�O�P�T�N*/</b><br><br><br>
                                  <font size="3" color="red">�W/�P�O�F��V�S��<b>�d�v</b>�ȕύX�_</font><br>
                                  <table bgcolor="#ffffff">
                                    <tbody>
                                      <tr>
                                        <td>���ւ񂱂��Ă�Ȃ�<br><br>
                                          <font color="red" size="5">��<s>�V�S�������ꗗ</s></font><br><br><br>
                                          �ȑO�̍X�V����<br>
                                          <a href="kousinnrireki.txt" target="_blank">������</a><br>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  �����m�点<br><br>
                                  <table bgcolor="#fff">
                                    <tbody>
                                      <tr>
                                        <td>���V�����I�i<a href="./ranking7.cgi" target="_blank">�ߋ����O</a>�j<br>
                                          �E<a href="ranking6.cgi?id=monamona" target="_blank">���i����</a>���v���t�B�[�����X�V���܂����B (12��0��0��)<br>
                                          �E<a href="ranking6.cgi?id=erwin" target="_blank">�����������R</a>���v���t�B�[�����X�V���܂����B (11��21��17��)<br>
                                          �E<a href="ranking6.cgi?id=monamona" target="_blank">���i����</a>���v���t�B�[�����X�V���܂����B (11��19��14��)<br>
                                          �E<a href="ranking6.cgi?id=monamona" target="_blank">���i����</a>���v���t�B�[�����X�V���܂����B (9��1��40��)<br>
                                          �E<a href="ranking6.cgi?id=shian" target="_blank">�����[��</a>���v���t�B�[�����X�V���܂����B (8��19��19��)<br>
                                          �E<a href="ranking6.cgi?id=monamona" target="_blank">���i����</a>���v���t�B�[�����X�V���܂����B (8��0��36��)<br>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <font size="4" color="red">�P/�Q�T�F�Q���P���Q�P�����Ƀ��Z�b�g��\�肵�Ă���܂��B��낵�����肢�������܂�</font><br>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <table bgcolor="#fff">
                    <tr>
                      <td valign="top">
                        <table bgcolor=$TABLE_C align=center border=0>
                          <form action="$FILE_STATUS" method="post">
                            <input type="hidden" name="mode" value="STATUS">
                            <tr>
                              <th bgcolor=$TD_C2 height=5>USER ID</th>
                              <td><input type="text" size="10" name="id" value="$_id"></td>
                            </tr>
                            <tr>
                              <th bgcolor=$TD_C2 height=5>PASS WORD</th>
                              <td><input type="password" size="10" name="pass" value="$_pass"></td>
                            </tr>
                            <tr>
                              <td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="���O�C��"></td>
                            </tr>
                          </form>
                        </table>
                      </td>
                      <td valign="top">
                        <table bgcolor="#842" align="center" border="0">
                          <tbody>
                            <tr>
                              <td bgcolor="#EFE0C0">
                                ���ݎc��<b>1</b>��<br>
                                ���݂̃��O�C���l���F<b>2</b>�l<br>
                                �莆���x�F<b>1401</b>�b�i�莆�P�ʂɂ����ω��b�ł��邩�j<br>
                                �莆���x�F<b>1</b>�ʁi�ߋ��P���Ԃɉ��ʂ̎莆���s�����������j<br>
                                <table bgcolor="#fff">
                                  <tbody>
                                    <tr>
                                      <td>�y�H�z<a href="./manual.html#14" target="_blank">�������Ƃ���</a><br>
                                        <font size="1">�E�h�c�A�o�v��Y�ꂽ�Ƃ�<br>
                                          �E�����ԃv���C�ł��Ȃ��ꍇ�̍폜��~�[�u�A�ȂǂȂ�<br>
                                        </font>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <table width=100% BGCOLOR=$TABLE_C  cellspacing=1>
                      <tbody>$mess</tbody>
                    </table>
                    <br>
                  </td></tr>
                  <tr>
                    <td bgcolor=#EFE0C0 colspan="2" width=80% height=20><font color=#8E4C28 size=2>$S_MES</font></td>
                  </tr>
                  <tr>
                    <td bgcolor=#EFE0C0 colspan="2" width=80% height=20><font color=#8E4C28 size=2>$D_MES</font></td>
                  </tr>
                  $ACT_MES
                </tbody></table>
              </tr>
            </table>

<form method=post action=./admin.cgi>
ID:<input type=text name=id size=7>
PASS:<input type=pass name=pass size=7>
<input type=submit value=�Ǘ���>
</form>

</center>

EOM

	&FOOTER;
	exit;

}
# _/_/_/_/_/_/_/_#
# ���ȃJ�E���^�[ #
# _/_/_/_/_/_/_/_#
sub COUNTER {

	$file_read = "$LOG_DIR/counter.cgi";
	open(IN,"$file_read") or &ERR2('�t�@�C�����J���܂���ł����B');
	@reading = <IN>;
	close(IN);

	($total_count) = split(/<>/,$reading[0]);
	$total_count++;

	&SAVE_DATA("$file_read","$total_count");
}
