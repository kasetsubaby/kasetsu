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

if($MENTE) { &ERR2("�����e�i���X���ł��B���΂炭���҂����������B"); }
&DECODE;
#if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("�A�h���X�o�[�ɒl����͂��Ȃ��ł��������B"); }
&RANKING;


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#      �Q���҃��X�g�n�o�d�m      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub RANKING {

	&SERVER_STOP;
	open(IN,"$COUNTRY_NO_LIST") or &ERR2('�t�@�C�����J���܂���ł����B');
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
				&ERR("�t�@�C���I�[�v���G���[�I");
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

	$best_list = "<TR><TD align=center>�^�C�g��</TD><TD align=center>���l</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";

	$point_list = "<TR><TD align=center>����</TD><TD align=center>����</TD><TD align=center>����</TD><TD align=center>�m��</TD><TD align=center>������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@POINT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#1'>����\�\\��No.1</a></TH><TH>$klpoint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
			$point_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$point_list .= "<TR><TD align=center>$i</TD><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[4]} @CL_DATA;
	@STR = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$str_list = "<TR><TD align=center>����</TD><TD align=center>����</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@STR){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#2'>����No.1</a></TH><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$str_list .= "<TR><TH><font color=blue>�y$i�z</font></TD><TH>$kstr</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$str_list .= "<TR><TD align=center>$i</TD><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[5]} @CL_DATA;
	@INT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$int_list = "<TR><TD align=center>����</TD><TD align=center>�m��</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@INT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#3'>�m��No.1</a></TH><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
			$int_list .= "<TR><TH><font color=blue>�y$i�z</TH><TH>$kint</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$int_list .= "<TR><TD align=center>$i</TD><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[6]} @CL_DATA;
	@LER = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$lea_list = "<TR><TD align=center>����</TD><TD align=center>������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@LER){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
		$lea_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$klea</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#4'>������No.1</a></TH><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$lea_list .= "<TR><TD align=center>$i</TD><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[7]} @CL_DATA;
	@CHA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$cha_list = "<TR><TD align=center>����</TD><TD align=center>�l�]</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@CHA){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#5'>�l�]No.1</a></TH><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$cha_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$kcha</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$cha_list .= "<TR><TD align=center>$i</TD><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[11]} @CL_DATA;
	@GOLD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$gold_list = "<TR><TD align=center>����</TD><TD align=center>��</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@GOLD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#6'>������No.1</a></TH><TH>��:$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$gold_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>��:$kgold</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$gold_list .= "<TR><TD align=center>$i</TD><TH>��:$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[12]} @CL_DATA;
	@RICE = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$rice_list = "<TR><TD align=center>����</TD><TD align=center>��</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@RICE){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#7'>����No.1</a></TH><TH>��:$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$rice_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>��:$krice</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$rice_list .= "<TR><TD align=center>$i</TD><TH>��:$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CLASS = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$class_list = "<TR><TD align=center>����</TD><TD align=center>�K���l</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@CLASS){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#8'>�K���lNo.1</a></TH><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$class_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$kclass</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$class_list .= "<TR><TD align=center>$i</TD><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#9'>�N�U����No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#10'>��쐬��No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#11'>�N�U���sNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#12'>������sNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#13'>��U��No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#14'>��ǔj��No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#15'>�s�s�x�zNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
  @DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

  $i=1;
  $dead_list = "<TR><TD align=center>����</TD><TD align=center>�|��������No.1</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
  foreach(@DEAD){
    ($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
    if($cou_name[$kcon] eq ""){
      $kcon_name= "������";
    }else{
      $kcon_name= "$cou_name[$kcon]";
    }
    if($knum eq ""){
      $knum=0;
    }
    if($i eq 1){
      $best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#16'>�|��������No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
    $dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
    }else{
    $dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
    }
    $i++;
    if($i>10){last;}
  }

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|��������No.1</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#16'>�|���ꂽ����No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#17'>���Q���zNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#18'>��Q���zNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#19'>����No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#20'>�h��No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#21'>����No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#22'>��No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#23'>�������zNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#24'>�p�lNo.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#25'>�U�ߑ�����No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#26'>���������No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

  @tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>����</TD><TD align=center>�|����������</TD><TD align=center colspan=2>���O</TD><TD align=center>��</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "������";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><a href='./ranking2.cgi#27'>�o�p����No.1</a></TH><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>�y$i�z</font></TH><TH>$knum�l</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knum�l</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name��</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	&HEADER;

	print <<"EOM";
  <b>�e�퍀�ڂɂ����镐���^�C�v�ʂ̕���</b>
  <table border="1">
  <tr><td>�l���i�S��89�l�j</td><td>����</td><td>�h�䗦</td><td>�^�������Q���󂯂����Q�i���傫�������ǂ��j�S��(1)</td><td>�n�m�� �S��(37��)</td></tr>
  <tr><td>
  ����15�l<br>
  ����26�l<br>
  �l�]��27�l<br>
  ������21�l<br>


  </td><td>
  ����47��<br>

  ����24��<br>

  �l�]��27��<br>

  ������48��<br>
  </td><td>
  ����29��<br>
  ����18��<br>
  �l�]��19��<br>
  ������38��<br>
  </td><td>
  ����1.25<br>
  ����0.91<br>
  �l�]��0.76<br>
  ������0.95<br>
  </td><td>
  ����45��<br>
  ����35��<br>
  �l�]��36��<br>
  ������37��<br>
  </td></tr>
  </table>

  <br><br>
  <table><tr><td>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�����̏������z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>����[%] </b>�i0%�`100%�j</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�����̏������z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>����[%] </b>�i0%�`100%�j</td></tr></table>

  <br>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�l�]���̏������z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>����[%] </b>�i0%�`100%�j</td></tr></table>
  <br>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�������̏������z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>����[%] </b>�i0%�`100%�j</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�S�̂̏������z</b></td></tr>
  <tr><td><div><p>�i�Q�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=65% width=5><br><img src="./image/img/bar3.gif" height=25% width=7 alt="5�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>����[%] </b>�i0%�`100%�j</td></tr></table>



  </td><td>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�����̖h�q�����z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=50% width=5><br><img src="./image/img/bar3.gif" height=40% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>�h�䗦[%] </b>�i0%�`100%�j</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�����̖h�䗦���z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>�h�䗦[%] </b>�i0%�`100%�j</td></tr></table>

  <br>

  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�l�]���̖h�䗦���z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>�h�䗦[%] </b>�i0%�`100%�j</td></tr></table>

  <br>
  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�������̖h�䗦���z</b></td></tr>
  <tr><td><div><p>�i�P�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=60% width=5><br><img src="./image/img/bar3.gif" height=30% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>�h�䗦[%] </b>�i0%�`100%�j</td></tr></table>
  <br>


  <table border=1>
  <tr><td></td><td colspan="1" align="center"><b>�S�̖̂h�q�����z</b></td></tr>
  <tr><td><div><p>�i�Q�O�l�`�O�l�j<br><b>�l��[�l]</b></p></div></td><td bgcolor="#ffffff" colspan="1">
  <table cellpadding=0 cellspacing="0" height=150 width=400><tr valign="bottom">
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>1</font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>21</font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=65% width=5><br><img src="./image/img/bar3.gif" height=25% width=7 alt="5�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1>41</font></td>
  <td><img src="./image/img/bar4.gif" height=70% width=5><br><img src="./image/img/bar3.gif" height=20% width=7 alt="4�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=65% width=5><br><img src="./image/img/bar3.gif" height=25% width=7 alt="5�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=75% width=5><br><img src="./image/img/bar3.gif" height=15% width=7 alt="3�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=80% width=5><br><img src="./image/img/bar3.gif" height=10% width=7 alt="2�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>61</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=85% width=5><br><img src="./image/img/bar3.gif" height=5% width=7 alt="1�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>81</font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1></font></td>
  <td><img src="./image/img/bar4.gif" height=90% width=5><br><img src="./image/img/bar3.gif" height=0% width=7 alt="0�l"><br><font size=1>99</font></td>
  </tr>
  </table>
  </td></tr>
  <tr><td></td><td align="center" width=350><b>�h�䗦[%] </b>�i0%�`100%�j</td></tr></table>


  </td></tr></table>
  <br>
  <B>���w�`����</b><br>
  	���؂̐w�F51.02��<br>
  	��̐w�F22.56��<br>
  	��s�̐w�F48.05��<br>
  	�ߗ��̐w�F62.28��<br>
  	�N��̐w�F59.97��<br>
  	���b�̐w�F41.5��<br>
  	���ւ̐w�F52.06��<br>
  	���~�̐w�F28.65��<br>
  	�Ԍ���̐w�F58.4��<br>
  	�Ղ̐w�F72.63��<br>
  	���n�̐w�F54.7��<br>
  	�ݐn�̐w�F34.49��<br>
  	�`���̐w�F54.34��<br>
  	�`�����I�b�g�F35.29��<br>
  	�t�@�����N�X�F��<br>
  	�Q�������`�F55.07��<br>
  <br>
  <table border="1">
  <tr><td>
  <b>�����ԕ�TOP�y�[�W�A�N�Z�X��</b><br>
  <select><option value="">�y2014�N5��5��0���z<option value="">�y2014�N5��5��1���z<option value="">�y2014�N5��5��2���z<option value="">�y2014�N5��5��3���z<option value="">�y2014�N5��5��4���z<option value="">�y2014�N5��5��5���z<option value="">�y2014�N5��5��6���z<option value="">�y2014�N5��5��7���z<option value="">�y2014�N5��5��8���z<option value="">�y2014�N5��5��9���z<option value="">�y2014�N5��5��10���z53<option value="">�y2014�N5��5��11���z171<option value="">�y2014�N5��5��12���z151<option value="">�y2014�N5��5��13���z214<option value="">�y2014�N5��5��14���z140<option value="">�y2014�N5��5��15���z151<option value="">�y2014�N5��5��16���z132<option value="">�y2014�N5��5��17���z230<option value="">�y2014�N5��5��18���z272<option value="">�y2014�N5��5��19���z811<option value="">�y2014�N5��5��20���z181<option value="">�y2014�N5��5��21���z233<option value="">�y2014�N5��5��22���z338<option value="">�y2014�N5��5��23���z487</select><br>
  </td>
  <td>
  <b>�����ԕʎ莆���M��</b><br>
  <select><option value="">�y2014�N5��5��0���z<option value="">�y2014�N5��5��1���z<option value="">�y2014�N5��5��2���z<option value="">�y2014�N5��5��3���z<option value="">�y2014�N5��5��4���z<option value="">�y2014�N5��5��5���z<option value="">�y2014�N5��5��6���z<option value="">�y2014�N5��5��7���z<option value="">�y2014�N5��5��8���z<option value="">�y2014�N5��5��9���z<option value="">�y2014�N5��5��10���z53<option value="">�y2014�N5��5��11���z171<option value="">�y2014�N5��5��12���z151<option value="">�y2014�N5��5��13���z214<option value="">�y2014�N5��5��14���z140<option value="">�y2014�N5��5��15���z151<option value="">�y2014�N5��5��16���z132<option value="">�y2014�N5��5��17���z230<option value="">�y2014�N5��5��18���z272<option value="">�y2014�N5��5��19���z811<option value="">�y2014�N5��5��20���z181<option value="">�y2014�N5��5��21���z233<option value="">�y2014�N5��5��22���z338<option value="">�y2014�N5��5��23���z487</select
  </td></tr></table>
EOM

	&FOOTER;

	exit;
}
