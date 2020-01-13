#_/_/_/_/_/_/_/_/_/#
#_/   新規登録   _/#
#_/_/_/_/_/_/_/_/_/#

sub ENTRY {

	&CHEACKER;
	&HEADER;

	open(IN,"$COUNTRY_MES") or &ERR("指定されたファイルが開けません。");
	@MES_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('ファイルを開けませんでした。err no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}

	$mess .= "<TR><TD BGCOLOR=$TD_C1 colspan=2>各国の新規参入者へのメッセージ</TD></TR>";
	foreach(@MES_DATA){
		($cmes,$cid)=split(/<>/);
		$mess .= "<TR><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cou_name[$cid]国</TD><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cmes</TD></TR>";
	}



	open(IN,"$TOWN_LIST") or &ERR("指定されたファイルが開けません。");
	@TOWN_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$t_list .= "<option value=\"$zc\">$z2name【$cou_name[$z2con]】";
		$zc++;
	}
	if($in{'url'} eq ""){$nurl = "http://";}else{$nurl = "$in{'url'}";}
	if($in{'mail'} eq ""){$nmail = "\@";}else{$nmail = "$in{'mail'}";}
	if(ATTESTATION){$emes = "↑入力しなくてもＯＫです。入力するとメール対応での本人確認がスムーズに行えます";}
	print <<"EOM";
	<script language="JavaScript">
		function changeImg(){
			num=document.para.chara.selectedIndex;
			document.Img.src="$IMG/"+ num +".gif";
		}
	</script>
<hr size=0><CENTER><font size=4><b>-- 武将登録 --</b></font><hr size=0><form action="$FILE_ENTRY" method="post" name=para><input type="hidden" name="mode" value="NEW_CHARA">
<table bgcolor=$TABLE_C width=80% border=0 cellpadding="1" cellspacing="1">$mess</table>

<table bgcolor=$TABLE_C border=0 cellpadding="3" cellspacong="1"><tr><TD colspan=2 bgcolor=$TD_C1>
* IDとPASSが同じ場合登録出来ません。<BR>
* IDは公開されているものと思って下さい（IDから連想できるようなPWは設定しないでください）<BR>
* ２重登録は出来ません<BR>
* 最大登録人数は$ENTRY_MAX名です。（現在登録者$num名）<BR>
* すべての項目を記入してください。<BR>
* <a href="./manual.html" TARGET="_blank">ゲーム説明</a>をよく読んでから参加してください。<BR>
* 登録されたメールアドレスには認証IDを送信しませんが、出来れば正しいアドでお願いします。<BR>
*初期位置に何処の支配もうけていない都市（【】空欄の都市）を選択すると君主として参加\可\能\です。それ以外はその街の所有者の配下になります。<a href="./ranking.cgi" TARGET="_blank">街一覧</a> <BR>
</TD></tr><tr bgcolor=$TD_C2><TD width=100>名 前</tD><tD bgcolor=$TD_C3><input type="text" name="chara_name" size="30" value="$in{'chara_name'}"><br>・武将の名前を入力してください。<BR>[全角大文字で１～１０文字以内]</tD></tr><tr><TD bgcolor=$TD_C2>イメージ</TD><TD bgcolor=$TD_C3><TABLE bgcolor=$TABLE_C border=2><TR><TD><img src=\"$IMG/0.gif\" name=\"Img\">
</TD></TR></TABLE><select name=chara onChange=\"changeImg()\">
EOM
	foreach (0..$CHARA_IMAGE){print "<option value=\"$_\">イメージ[$_]\n";}
	print <<"EOM";
</select><br>・武将のイメージを選んでください。<br>
<b>※登録後でも自由に変更できます。アイコンUPローダーも設置しており、好きな画像をアイコンとして使用することも\可\能\です！</b><br>
<s>全イメージリスト</s></TH></tr>

<tr bgcolor=$TD_C2><TD>初期位置</TD><TD bgcolor=$TD_C3><select name="con">
<option value=""> 選択してください
$t_list
</select><br>・所属する国を選んでください。（【】は建国可\能\)<br>
・<font color="red">リセット直後(更新開始後１日間、つまりリセット日から２日)は仕官制限で、１国につき８人までしか仕官できません。よくご確認ください。<br>
<b>国ごとの人数はこちらで確認してください→<a href="ranking.cgi" target="_blank">こちら</b></a></font></TD></tr><tr><TD bgcolor=$TD_C2>ID</TD><TD bgcolor=$TD_C3><input type="text" name="id" size="10" value="$in{'id'}"><br>・参加する希望IDを記入してください。<BR>[半角英数字で４～８文字以内]</TD></tr><tr><TD bgcolor=$TD_C2>パスワード</TD><TD bgcolor=$TD_C3><input type="password" name="pass" size="10"  value="$in{'pass'}"><br>・パスワードを登録してください。<BR>[半角英数字で４～８文字以内]</TD></tr>
<tr><TD bgcolor=$TD_C2>\能\力</TD><TD bgcolor=$TD_C3><table><TR><TD>武力</TD><TD><input type="text" name="str" size="5">[5～100]</TD></TR><TR><TD>知力</TD><TD><input type="text" name="int" size="5">[5～100]</TD></TR><TR><TD>統率力（兵士を雇える数です。最低６０以上にすることをおすすめします）</TD><TD><input type="text" name="tou" size="5">[5～100]</TD></TR><TR><TD>人望</TD><TD><input type="text" name="cha" size="5">[5～100]</TD></TR></TABLE>・\能\力を指定して下さい。。<BR>[全部の合計が150になるようにして下さい。]<br><br>※途中登録者には、階級値や金、米、スキルポイントなどのボーナスがあります。<br>※いつ登録してもそこそこ戦えるようにはしてあるつもりです！<br><br><b>※このゲームにあまり慣れていない方は１つのパラメータに特化させることをオススメします。</b><br><table bgcolor="#ffffff"><tbody><tr><td>※このゲームでは、武力の値が５であろうと、問題なく戦争で活躍できます。様々な兵種が用意されているので色々試してみましょう<br>
↓入力例↓<br>
■武力１００、知力５、統率６５、人望５<br>
→武力に特化させれば、平時では城壁の建設、戦時では花形として大いに活躍できるでしょう<br>
<br>
■武力５、知力１００、統率６５、人望５<br>
→知力に特化させれば、平時の内政コマンドで有利になり、戦争では多彩なスキルを駆使して変則的な戦い方で活躍できます。<br>
<br>
■武力６５、知力５、統率１００、人望５<br>
→統率力に特化させれば、兵士を大量に雇うことができ、単純な物量戦から、統率力を活かしたスキルで戦ったりできます。また、特に序盤での活躍は大いに期待できるでしょう<br>
<br>
■武力５、知力５、統率６５、人望１００<br>
→人望に特化させれば、知力特化型と同様にトリッキーな戦いができるほか、戦争中でも米施しさえしていれば国へ貢献できるので、あまりゲームに時間をとれない人にもオススメです。<br>
</td></tr></tbody></table></TD></tr>

<tr><TD bgcolor=$TD_C2>メールアドレス</TD><TD bgcolor=$TD_C3><input type="text" name="mail" size="35" value="$nmail"><br> $emes</TD></tr>
</table>
<BR>
<TABLE width=80% bgcolor=$TABLE_C>
<tr><TH bgcolor=$TD_C3 colspan=2>君主</TH></TR>
<tr><TD bgcolor=$TD_C1 colspan=2>
・所属位置に*がついている場合はこちらも登録してください。<br>
<b><font color="red">・初期ではログが流れやすいので宣戦布告が無いかを勢力図で確かめるように気をつけてくださいね。<br>
※布告文の確認し忘れにより損害を被った場合などは自己責任でお願いします※
<br>
<br>
<br>
■建国した人には以下のボーナスが追加されます！<br>
・金＋２０００<br>
・米＋２０００<br>
・階級値＋２００<br>
・武器＋１<br>
・防具＋１<br>
・旗＋１<br>
・書物＋１<br>
<br>
</font></b>
</TD></TR>
<tr bgcolor=$TD_C1><TD width=100>国名</tD><tD bgcolor=$TD_C3><input type="text" name="cou_name" size="30" value="$in{'cou_name'}">
<select name="cou_namegobi">
<option value="国"> 国
</option><option value="族"> 族
</option><option value="組"> 組
</option><option value="党"> 党
</option><option value="会社"> 会社
</option><option value="隊"> 隊
</option><option value="軍"> 軍
</option><option value="部"> 部
</option><option value="課"> 課
</option><option value="部隊"> 部隊
</option><option value="教"> 教
</option><option value="属"> 属
</option><option value="団"> 団
</option><option value="師団"> 師団
</option><option value="家"> 家
</option><option value="王朝"> 王朝
</option><option value="朝"> 朝
</option><option value="省"> 省
</option><option value="庁"> 庁
</option><option value="軍団"> 軍団
</option><option value="丸"> 丸
</option><option value="神"> 神
</option><option value="派"> 派
</option><option value="組合"> 組合
</option><option value="賊"> 賊
</option><option value=""> 末尾無し


</option></select><br>・新国家の名称を決めてください。<BR>[全角大文字で１～１２文字以内]</tD></tr>
<tr><TD bgcolor=$TD_C1>国色</TD><TD bgcolor=$TD_C3>
EOM
	$i=0;
	foreach(@ELE_BG){print "<input type=radio name=ele value=\"$i\"><font color=$ELE_BG[$i]>■</font> \n";$i++;}
	print <<"EOM";
<br>・国の色を決めてください。</TD></tr>
</TABLE>

</table>
</td></tr>
<tr><TH align="center" bgcolor=$TABLE_C><a href="http://densetu.sakura.ne.jp/manual.html#12" target="_blank">利用規約（ルール）</a><br><input type="submit" value="利用規約に同意して登録"></TH></tr></table></form></CENTER>

EOM

	# フッター表示
	&FOOTER;

	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/   参加登録者上限チェック   _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("ファイルオープンエラー！");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("最大登録数\[$ENTRY_MAX\]を超えています。現在新規登録出来ません。");
		}
	}
}
1;
