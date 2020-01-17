#_/_/_/_/_/_/_/_/#
#      鍛錬      #
#_/_/_/_/_/_/_/_/#

sub TANREN {

	$ksub2=0;
	if($kgold < 50){
		&K_LOG("$mmonth月:金が足りません。");
	}else{
		if($cnum eq "1"){
			$kstr_ex +=2;
			$a_mes = "武力";
		}elsif($cnum eq "2"){
			$kint_ex +=2;
			$a_mes = "知力";
		}else{
			$klea_ex +=2;
			$a_mes = "統率力";
		}
		$kgold-=50;
		$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
		&K_LOG("$mmonth月:$a_mesを強化しました。");
	}

}
1;
