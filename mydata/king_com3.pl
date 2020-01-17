#_/_/_/_/_/_/_/_/_/_/#
#        徴兵２      #
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM3 {

	if($in{'sel'} eq ""){&ERR("任命相手が入力されていません。");}
	if($in{'type'} eq ""){&ERR("対象が入力されていません。");}
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	open(IN,"./charalog/main/$in{'sel'}.cgi") || &ERR("そのIDは存在しません。");
	@E_DATA = <IN>;
	close(IN);

	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);

	if($econ ne $kcon){
		&ERR("国が違います。");
	}

	if($in{'type'} eq "0"){
		$xgunshi = $eid;
		$tname = "軍師";
	}elsif($in{'type'} eq "1"){
		$xdai = $eid;
		$tname = "大将軍";
	}elsif($in{'type'} eq "2"){
		$xuma = $eid;
		$tname = "騎馬将軍";
	}elsif($in{'type'} eq "3"){
		$xgoei = $eid;
		$tname = "護衛将軍";
	}elsif($in{'type'} eq "4"){
		$xyumi = $eid;
		$tname = "弓将軍";
	}elsif($in{'type'} eq "5"){
		$xhei = $eid;
		$tname = "将軍";
	}
	$xsub = "$xgunshi,$xdai,$xuma,$xgoei,$xyumi,$xhei,$xxsub1,$xxsub2,";

	&COUNTRY_DATA_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$tnameに$enameを任命しました。</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="ＯＫ"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;
