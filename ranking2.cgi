#!/usr/bin/env perl

#################################################################
#   【免責事項】                                                #
#    このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
#    また設置に関する質問はサポート掲示板にお願いいたします。   #
#    直接メールによる質問は一切お受けいたしておりません。       #
#################################################################

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
$a
<CENTER><TABLE WIDTH="80%" height=100% bgcolor=$TABLE_C>
<TBODY><TR><TD BGCOLOR=$TD_C1 WIDTH=100% height=100% align=center>
<BR>
<b>※名将タイトルをクリックすると対応するＴＯＰ１０が表示されます</b>
<TABLE border=1 width=90% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH bgcolor=#284422><font size=5 color=CCDDCC>- 名 将 一 覧 -</font></TH></TR>
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>大陸の英雄</font></TH></TR>
$best_list
</TBODY></TABLE>

<BR><p>
<a name="1"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=8 bgcolor=#446644><font size=4 color=CCDDCC>名将　１０選</font></TH></TR>
$point_list
</TBODY></TABLE>

<BR><p>
<a name="2"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>豪傑　１０選</font></TH></TR>
$str_list
</TBODY></TABLE>

<BR><p>
<a name="3"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>秀才　１０選</font></TH></TR>
$int_list
</TBODY></TABLE>

<BR><p>
<a name="4"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>指揮　１０選</font></TH></TR>
$lea_list
</TBODY></TABLE>

<BR><p>
<a name="5"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>魅力　１０選</font></TH></TR>
$cha_list
</TBODY></TABLE>

<BR><p>
<a name="6"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>富豪　１０選</font></TH></TR>
$gold_list
</TBODY></TABLE>

<BR><p>
<a name="7"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>穀物　１０選</font></TH></TR>
$rice_list
</TBODY></TABLE>

<BR><p>
<a name="8"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>功労者　１０選</font></TH></TR>
$class_list
</TBODY></TABLE>

<BR><p>
<a name="9"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>闘神　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="10"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>守護神　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="11"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>侵攻失敗武将　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="12"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>守備失敗武将　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="13"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>城攻め回数　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="14"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>城壁破壊　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="15"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>都市支配神　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="16"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>倒した兵数　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="17"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>倒された人数　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="18"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>相手への損害総額　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="19"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>自分の被害総額　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="20"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>武器　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="21"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>防具　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="22"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>書物　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="23"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>旗　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="24"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>国庫献金総額　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="25"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>ON率　１０選　(100%の人は含みません)</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="26"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>勝率（攻め側）　１０選 (100%の人は含みません)</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="27"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>勝率（守備側）　１０選(100%の人は含みません)</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="28"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>登用成功　１０選</font></TH></TR>
$dead_list
</TBODY></TABLE>


<form action="$FILE_TOP" method="post">
<input type=submit value="メニューに戻る"></form>

      </TD>
    </TR>
  </TBODY>
</TABLE>
<b>各種項目における武将タイプ別の平均</b>
<table border="1">
<tbody><tr><td>人数（全体89人）</td><td>勝率</td><td>防御率</td><td>与えた損害÷受けた損害（※大きい方が良い）全体(1)</td><td>ＯＮ率 全体(37％)</td></tr>
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
</tbody></table>
EOM

	&FOOTER;

	exit;
}
