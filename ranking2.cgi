#!/usr/bin/env perl

#################################################################
#   y–ÆÓ–€z                                                #
#    ‚±‚ÌƒXƒNƒŠƒvƒg‚ÍƒtƒŠ[ƒ\ƒtƒg‚Å‚·B‚±‚ÌƒXƒNƒŠƒvƒg‚ğg—p‚µ‚½ #
#    ‚¢‚©‚È‚é‘¹ŠQ‚É‘Î‚µ‚ÄìÒ‚ÍˆêØ‚ÌÓ”C‚ğ•‰‚¢‚Ü‚¹‚ñB         #
#    ‚Ü‚½İ’u‚ÉŠÖ‚·‚é¿–â‚ÍƒTƒ|[ƒgŒf¦”Â‚É‚¨Šè‚¢‚¢‚½‚µ‚Ü‚·B   #
#    ’¼Úƒ[ƒ‹‚É‚æ‚é¿–â‚ÍˆêØ‚¨ó‚¯‚¢‚½‚µ‚Ä‚¨‚è‚Ü‚¹‚ñB       #
#################################################################

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("ƒƒ“ƒeƒiƒ“ƒX’†‚Å‚·B‚µ‚Î‚ç‚­‚¨‘Ò‚¿‚­‚¾‚³‚¢B"); }
&DECODE;
#if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("ƒAƒhƒŒƒXƒo[‚É’l‚ğ“ü—Í‚µ‚È‚¢‚Å‚­‚¾‚³‚¢B"); }
&RANKING;


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#      Q‰ÁÒƒŠƒXƒg‚n‚o‚d‚m      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub RANKING {

	&SERVER_STOP;
	open(IN,"$COUNTRY_NO_LIST") or &ERR2('ƒtƒ@ƒCƒ‹‚ğŠJ‚¯‚Ü‚¹‚ñ‚Å‚µ‚½B');
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
				&ERR("ƒtƒ@ƒCƒ‹ƒI[ƒvƒ“ƒGƒ‰[I");
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

	$best_list = "<TR><TD align=center>ƒ^ƒCƒgƒ‹</TD><TD align=center>”’l</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";

	$point_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>‘‡</TD><TD align=center>•—Í</TD><TD align=center>’m—Í</TD><TD align=center>“—¦—Í</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@POINT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#1'>‘‡\”\\—ÍNo.1</a></TH><TH>$klpoint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
			$point_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$point_list .= "<TR><TD align=center>$i</TD><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[4]} @CL_DATA;
	@STR = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$str_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>•—Í</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@STR){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#2'>•—ÍNo.1</a></TH><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$str_list .= "<TR><TH><font color=blue>y$iz</font></TD><TH>$kstr</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$str_list .= "<TR><TD align=center>$i</TD><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[5]} @CL_DATA;
	@INT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$int_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>’m—Í</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@INT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#3'>’m—ÍNo.1</a></TH><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
			$int_list .= "<TR><TH><font color=blue>y$iz</TH><TH>$kint</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$int_list .= "<TR><TD align=center>$i</TD><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[6]} @CL_DATA;
	@LER = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$lea_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“—¦—Í</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@LER){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
		$lea_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$klea</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#4'>“—¦—ÍNo.1</a></TH><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$lea_list .= "<TR><TD align=center>$i</TD><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[7]} @CL_DATA;
	@CHA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$cha_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>l–]</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@CHA){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#5'>l–]No.1</a></TH><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$cha_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$kcha</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$cha_list .= "<TR><TD align=center>$i</TD><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[11]} @CL_DATA;
	@GOLD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$gold_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>‹à</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@GOLD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#6'>Š‹àNo.1</a></TH><TH>‹à:$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$gold_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>‹à:$kgold</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$gold_list .= "<TR><TD align=center>$i</TD><TH>‹à:$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[12]} @CL_DATA;
	@RICE = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$rice_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>•Ä</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@RICE){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#7'>’•¨No.1</a></TH><TH>•Ä:$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$rice_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>•Ä:$krice</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$rice_list .= "<TR><TD align=center>$i</TD><TH>•Ä:$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CLASS = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$class_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>ŠK‹‰’l</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@CLASS){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#8'>ŠK‹‰’lNo.1</a></TH><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$class_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$kclass</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$class_list .= "<TR><TD align=center>$i</TD><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#9'>NU¬Œ÷No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#10'>çŒì¬Œ÷No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#11'>NU¸”sNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#12'>ç”õ¸”sNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#13'>éU‚ßNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#14'>é•Ç”j‰óNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#15'>“ssx”zNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
  @DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

  $i=1;
  $dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•º”No.1</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
  foreach(@DEAD){
    ($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
    if($cou_name[$kcon] eq ""){
      $kcon_name= "–³Š‘®";
    }else{
      $kcon_name= "$cou_name[$kcon]";
    }
    if($knum eq ""){
      $knum=0;
    }
    if($i eq 1){
      $best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#16'>“|‚µ‚½•º”No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
    $dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
    }else{
    $dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
    }
    $i++;
    if($i>10){last;}
  }

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•º”No.1</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#16'>“|‚³‚ê‚½•º”No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#17'>‘¹ŠQ‘ŠzNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#18'>”íŠQ‘ŠzNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#19'>•ŠíNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#20'>–h‹ïNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#21'>‘•¨No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#22'>ŠøNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#23'>Œ£‹à‘ŠzNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#24'>”plNo.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#25'>U‚ß‘¤Ÿ—¦No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#26'>ç”õ‘¤Ÿ—¦No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>‡ˆÊ</TD><TD align=center>“|‚µ‚½•«”</TD><TD align=center colspan=2>–¼‘O</TD><TD align=center>‘</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "–³Š‘®";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#27'>“o—p¬Œ÷No.1</a></TH><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>y$iz</font></TH><TH>$knuml</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knuml</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name‘</TD></TR>";
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
<b>¦–¼«ƒ^ƒCƒgƒ‹‚ğƒNƒŠƒbƒN‚·‚é‚Æ‘Î‰‚·‚é‚s‚n‚o‚P‚O‚ª•\¦‚³‚ê‚Ü‚·</b>
<TABLE border=1 width=90% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH bgcolor=#284422><font size=5 color=CCDDCC>- –¼ « ˆê —— -</font></TH></TR>
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>‘å—¤‚Ì‰p—Y</font></TH></TR>
$best_list
</TBODY></TABLE>

<BR><p>
<a name="1"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=8 bgcolor=#446644><font size=4 color=CCDDCC>–¼«@‚P‚O‘I</font></TH></TR>
$point_list
</TBODY></TABLE>

<BR><p>
<a name="2"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>‹Œ†@‚P‚O‘I</font></TH></TR>
$str_list
</TBODY></TABLE>

<BR><p>
<a name="3"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>GË@‚P‚O‘I</font></TH></TR>
$int_list
</TBODY></TABLE>

<BR><p>
<a name="4"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>wŠö@‚P‚O‘I</font></TH></TR>
$lea_list
</TBODY></TABLE>

<BR><p>
<a name="5"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>–£—Í@‚P‚O‘I</font></TH></TR>
$cha_list
</TBODY></TABLE>

<BR><p>
<a name="6"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>•x‹@‚P‚O‘I</font></TH></TR>
$gold_list
</TBODY></TABLE>

<BR><p>
<a name="7"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>’•¨@‚P‚O‘I</font></TH></TR>
$rice_list
</TBODY></TABLE>

<BR><p>
<a name="8"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>Œ÷˜JÒ@‚P‚O‘I</font></TH></TR>
$class_list
</TBODY></TABLE>

<BR><p>
<a name="9"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>“¬_@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="10"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>çŒì_@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="11"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>NU¸”s•«@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="12"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>ç”õ¸”s•«@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="13"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>éU‚ß‰ñ”@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="14"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>é•Ç”j‰ó@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="15"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>“ssx”z_@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="16"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>“|‚µ‚½•º”@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="17"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>“|‚³‚ê‚½l”@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="18"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>‘Šè‚Ö‚Ì‘¹ŠQ‘Šz@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="19"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>©•ª‚Ì”íŠQ‘Šz@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="20"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>•Ší@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="21"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>–h‹ï@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="22"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>‘•¨@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="23"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>Šø@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="24"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>‘ŒÉŒ£‹à‘Šz@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="25"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>ON—¦@‚P‚O‘I@(100%‚Ìl‚ÍŠÜ‚İ‚Ü‚¹‚ñ)</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="26"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>Ÿ—¦iU‚ß‘¤j@‚P‚O‘I (100%‚Ìl‚ÍŠÜ‚İ‚Ü‚¹‚ñ)</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="27"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>Ÿ—¦iç”õ‘¤j@‚P‚O‘I(100%‚Ìl‚ÍŠÜ‚İ‚Ü‚¹‚ñ)</font></TH></TR>
$dead_list
</TBODY></TABLE>

<BR><p>
<a name="28"></a>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>“o—p¬Œ÷@‚P‚O‘I</font></TH></TR>
$dead_list
</TBODY></TABLE>


<form action="$FILE_TOP" method="post">
<input type=submit value="ƒƒjƒ…[‚É–ß‚é"></form>

      </TD>
    </TR>
  </TBODY>
</TABLE>
<b>Šeí€–Ú‚É‚¨‚¯‚é•«ƒ^ƒCƒv•Ê‚Ì•½‹Ï</b>
<table border="1">
<tbody><tr><td>l”i‘S‘Ì89lj</td><td>Ÿ—¦</td><td>–hŒä—¦</td><td>—^‚¦‚½‘¹ŠQ€ó‚¯‚½‘¹ŠQi¦‘å‚«‚¢•û‚ª—Ç‚¢j‘S‘Ì(1)</td><td>‚n‚m—¦ ‘S‘Ì(37“)</td></tr>
<tr><td>
•Š¯15l<br>
•¶Š¯26l<br>
l–]Š¯27l<br>
“—¦Š¯21l<br>


</td><td>
•Š¯47“<br>

•¶Š¯24“<br>

l–]Š¯27“<br>

“—¦Š¯48“<br>
</td><td>
•Š¯29“<br>
•¶Š¯18“<br>
l–]Š¯19“<br>
“—¦Š¯38“<br>
</td><td>
•Š¯1.25<br>
•¶Š¯0.91<br>
l–]Š¯0.76<br>
“—¦Š¯0.95<br>
</td><td>
•Š¯45“<br>
•¶Š¯35“<br>
l–]Š¯36“<br>
“—¦Š¯37“<br>
</td></tr>
</tbody></table>
EOM

	&FOOTER;

	exit;
}
