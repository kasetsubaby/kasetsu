#_/_/_/_/_/_/_/_/_/_/#
#      城の守備      #
#_/_/_/_/_/_/_/_/_/_/#

sub TOWN_DEF {

	$ksub2=0;
	if($ksol eq "0" || $ksol eq ""){
		&K_LOG("$mmonth月:兵０では守備につけません。");
	}else{
		open(IN,"$DEF_LIST");
		@DEF_LIST = <IN>;
		close(IN);
		my @NEW_DEF_LIST2=();
		$whit=0;
		foreach(@DEF_LIST){
			($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
			if("$tid" eq "$kid"){
			}else{
				push(@NEW_DEF_LIST2,"$_");
			}
		}
		unshift(@NEW_DEF_LIST2,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
		open(OUT,">$DEF_LIST");
		print OUT @NEW_DEF_LIST2;
		close(OUT);
		$kcex += 25;
		&K_LOG("$mmonth月:$znameの守備につきました。");
		$klea_ex++;
		$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
	}

}
1;
