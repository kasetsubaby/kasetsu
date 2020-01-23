#!/usr/bin/env perl

#################################################################
#   【免責事項】                                                #
#    このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
#    また設置に関する質問はサポート掲示板にお願いいたします。   #
#    直接メールによる質問は一切お受けいたしておりません。       #
#################################################################

use FindBin;
use lib $FindBin::Bin;

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("メンテナンス中です。しばらくお待ちください。"); }
&DECODE;
#if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("アドレスバーに値を入力しないでください。"); }
&RANKING;


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#      参加者リストＯＰＥＮ      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub RANKING {

	&SERVER_STOP;
	open(IN,"$COUNTRY_NO_LIST") or &ERR2('ファイルを開けませんでした。');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=1;

	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		$cou_name[$country_no]="$xname";
		$country_no++;
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("ファイルオープンエラー！");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$page[0]);
			($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$ktec1,$ktec2,$ktec3,$kvsub1,$kvsub2,) = split(/,/,$ksub1);
			$lpoint = $kstr+$kint+$klea;
			push(@CL_DATA,"$kid<>$kpass<>$kname<>$kchara<>$kstr<>$kint<>$klea<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$kpos<>$kmes<>$khost<>$kdate<>$kmail<>$kos<>$lpoint<>$ksub2_ex<>\n");
		}
	}
	closedir(dirlist);



	@tmp = map {(split /<>/)[26]} @CL_DATA;
	@POINT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;

	$best_list = "<TR><TD align=center>タイトル</TD><TD align=center>数値</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";

	$point_list = "<TR><TD align=center>順位</TD><TD align=center>総合</TD><TD align=center>武力</TD><TD align=center>知力</TD><TD align=center>統率力</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@POINT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#1'>総合\能\力No.1</a></TH><TH>$klpoint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
			$point_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$point_list .= "<TR><TD align=center>$i</TD><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[4]} @CL_DATA;
	@STR = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$str_list = "<TR><TD align=center>順位</TD><TD align=center>武力</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@STR){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#2'>武力No.1</a></TH><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$str_list .= "<TR><TH><font color=blue>【$i】</font></TD><TH>$kstr</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$str_list .= "<TR><TD align=center>$i</TD><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[5]} @CL_DATA;
	@INT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$int_list = "<TR><TD align=center>順位</TD><TD align=center>知力</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@INT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#3'>知力No.1</a></TH><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
			$int_list .= "<TR><TH><font color=blue>【$i】</TH><TH>$kint</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$int_list .= "<TR><TD align=center>$i</TD><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[6]} @CL_DATA;
	@LER = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$lea_list = "<TR><TD align=center>順位</TD><TD align=center>統率力</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@LER){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
		$lea_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$klea</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#4'>統率力No.1</a></TH><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$lea_list .= "<TR><TD align=center>$i</TD><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[7]} @CL_DATA;
	@CHA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$cha_list = "<TR><TD align=center>順位</TD><TD align=center>人望</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@CHA){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#5'>人望No.1</a></TH><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$cha_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$kcha</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$cha_list .= "<TR><TD align=center>$i</TD><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[11]} @CL_DATA;
	@GOLD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$gold_list = "<TR><TD align=center>順位</TD><TD align=center>金</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@GOLD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#6'>所持金No.1</a></TH><TH>金:$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$gold_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>金:$kgold</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$gold_list .= "<TR><TD align=center>$i</TD><TH>金:$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[12]} @CL_DATA;
	@RICE = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$rice_list = "<TR><TD align=center>順位</TD><TD align=center>米</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@RICE){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#7'>穀物No.1</a></TH><TH>米:$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$rice_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>米:$krice</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$rice_list .= "<TR><TD align=center>$i</TD><TH>米:$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CLASS = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$class_list = "<TR><TD align=center>順位</TD><TD align=center>階級値</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@CLASS){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#8'>階級値No.1</a></TH><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$class_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$kclass</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$class_list .= "<TR><TD align=center>$i</TD><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#9'>侵攻成功No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#10'>守護成功No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#11'>侵攻失敗No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#12'>守備失敗No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#13'>城攻めNo.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#14'>城壁破壊No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#15'>都市支配No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
  @DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

  $i=1;
  $dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した兵数No.1</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
  foreach(@DEAD){
    ($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
    if($cou_name[$kcon] eq ""){
      $kcon_name= "無所属";
    }else{
      $kcon_name= "$cou_name[$kcon]";
    }
    if($knum eq ""){
      $knum=0;
    }
    if($i eq 1){
      $best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#16'>倒した兵数No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
    $dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
    }else{
    $dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
    }
    $i++;
    if($i>10){last;}
  }

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した兵数No.1</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#16'>倒された兵数No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#17'>損害総額No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#18'>被害総額No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#19'>武器No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#20'>防具No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#21'>書物No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#22'>旗No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#23'>献金総額No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#24'>廃人No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#25'>攻め側勝率No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#26'>守備側勝率No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>順位</TD><TD align=center>倒した武将数</TD><TD align=center colspan=2>名前</TD><TD align=center>国</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "無所属";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#27'>登用成功No.1</a></TH><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>【$i】</font></TH><TH>$knum人</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum人</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name国</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	&HEADER;

	print <<"EOM";
  <b>各種項目における武将タイプ別の平均</b>
  <table border="1">
  <tr><td>人数（全体89人）</td><td>勝率</td><td>防御率</td><td>与えた損害÷受けた損害（※大きい方が良い）全体(1)</td><td>ＯＮ率 全体(37％)</td></tr>
  <tr><td>
  武官15人<br>
  文官26人<br>
  人望官27人<br>
  統率官21人<br>


  </td><td>
  武官47％<br>

  文官24％<br>

  人望官27％<br>

  統率官48％<br>
  </td><td>
  武官29％<br>
  文官18％<br>
  人望官19％<br>
  統率官38％<br>
  </td><td>
  武官1.25<br>
  文官0.91<br>
  人望官0.76<br>
  統率官0.95<br>
  </td><td>
  武官45％<br>
  文官35％<br>
  人望官36％<br>
  統率官37％<br>
  </td></tr>
  </table>

  <br><br>
  <table><tr><td>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>武官の勝率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>勝率[%] </b>（0%〜100%）</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>文官の勝率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>勝率[%] </b>（0%〜100%）</td></tr></table>

  <br>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>人望官の勝率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>勝率[%] </b>（0%〜100%）</td></tr></table>
  <br>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>統率官の勝率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>勝率[%] </b>（0%〜100%）</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>全体の勝率分布</b></td></tr>
  <tr><td><div><p>（２０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=65% width=5><br><img src="./image/img/bar3.gif" height=25% width=7 alt="5人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>勝率[%] </b>（0%〜100%）</td></tr></table>



  </td><td>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>武官の防衛率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=50% width=5><br><img src="./image/img/bar3.gif" height=40% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>防御率[%] </b>（0%〜100%）</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>文官の防御率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>防御率[%] </b>（0%〜100%）</td></tr></table>

  <br>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>人望官の防御率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>防御率[%] </b>（0%〜100%）</td></tr></table>

  <br>
  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>統率官の防御率分布</b></td></tr>
  <tr><td><div><p>（１０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>防御率[%] </b>（0%〜100%）</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>全体の防衛率分布</b></td></tr>
  <tr><td><div><p>（２０人〜０人）<br><b>人数[人]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=65% width=5><br><img src="./image/img/bar3.gif" height=25% width=7 alt="5人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=65% width=5><br><img src="./image/img/bar3.gif" height=25% width=7 alt="5人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0人"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>防御率[%] </b>（0%〜100%）</td></tr></table>


  </td></tr></table>
  <br>
  <B>◆陣形勝率</b><br>
  	魚鱗の陣：51.02％<br>
  	偃月の陣：22.56％<br>
  	雁行の陣：48.05％<br>
  	鶴翼の陣：62.28％<br>
  	鋒矢の陣：59.97％<br>
  	衝軛の陣：41.5％<br>
  	長蛇の陣：52.06％<br>
  	方円の陣：28.65％<br>
  	車懸りの陣：58.4％<br>
  	虎の陣：72.63％<br>
  	諸刃の陣：54.7％<br>
  	鈍刃の陣：34.49％<br>
  	伝説の陣：54.34％<br>
  	チャリオット：35.29％<br>
  	ファランクス：％<br>
  	ゲリラ隊形：55.07％<br>
  <br>
  <table border="1">
  <tr><td>
  <b>■時間別TOPページアクセス数</b><br>
  <select><option value="">【2014年5月5日0時】<option value="">【2014年5月5日1時】<option value="">【2014年5月5日2時】<option value="">【2014年5月5日3時】<option value="">【2014年5月5日4時】<option value="">【2014年5月5日5時】<option value="">【2014年5月5日6時】<option value="">【2014年5月5日7時】<option value="">【2014年5月5日8時】<option value="">【2014年5月5日9時】<option value="">【2014年5月5日10時】53<option value="">【2014年5月5日11時】171<option value="">【2014年5月5日12時】151<option value="">【2014年5月5日13時】214<option value="">【2014年5月5日14時】140<option value="">【2014年5月5日15時】151<option value="">【2014年5月5日16時】132<option value="">【2014年5月5日17時】230<option value="">【2014年5月5日18時】272<option value="">【2014年5月5日19時】811<option value="">【2014年5月5日20時】181<option value="">【2014年5月5日21時】233<option value="">【2014年5月5日22時】338<option value="">【2014年5月5日23時】487</select><br>
  </td>
  <td>
  <b>■時間別手紙送信数</b><br>
  <select><option value="">【2014年5月5日0時】<option value="">【2014年5月5日1時】<option value="">【2014年5月5日2時】<option value="">【2014年5月5日3時】<option value="">【2014年5月5日4時】<option value="">【2014年5月5日5時】<option value="">【2014年5月5日6時】<option value="">【2014年5月5日7時】<option value="">【2014年5月5日8時】<option value="">【2014年5月5日9時】<option value="">【2014年5月5日10時】53<option value="">【2014年5月5日11時】171<option value="">【2014年5月5日12時】151<option value="">【2014年5月5日13時】214<option value="">【2014年5月5日14時】140<option value="">【2014年5月5日15時】151<option value="">【2014年5月5日16時】132<option value="">【2014年5月5日17時】230<option value="">【2014年5月5日18時】272<option value="">【2014年5月5日19時】811<option value="">【2014年5月5日20時】181<option value="">【2014年5月5日21時】233<option value="">【2014年5月5日22時】338<option value="">【2014年5月5日23時】487</select
  </td></tr></table>
EOM

	&FOOTER;

	exit;
}
