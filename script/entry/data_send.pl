#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/     NEW CHARA DATA 作成    _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub DATA_SEND {

	open(IN,"$TOWN_LIST") or &ERR2("指定されたファイルが開けません。");
	@TOWN = <IN>;
	close(IN);

	&CHARA_MAIN_OPEN;
	&HEADER;

	print <<"EOM";
<CENTER><h3>＞＞登録完了＜＜</h3>
<hr size=0>
$knameで$GAME_TITLEの世界に登録されました。<BR>IDとPASSを忘れないようにメモして置いて下さい。
<hr size=0>
ID：<font color=red>$in{'id'}</font><BR>
PASS ：<font color=red>$in{'pass'}</font><BR>
<p>
ステータス<BR><table border=0 bgcolor=$TABLE_C cellspacing=1><TBODY bgcolor=$TD_C4>
<tr><td rowspan="8" align="center"><img src="$IMG/$in{'chara'}.gif"></td>
<td class="b1">名前</td><td>$in{'chara_name'}</td>
<td class="b1">国</td><td>$cou_name</td></tr>
<tr><td class="b1">階級</td><td>$LANK[0]</td>
<td class="b1">初期位置</td><td>$z2name</td></tr>
<tr><td class="b1">武力</td><td>$in{'str'}</td>
<td class="b1">知力</td><td>$in{'int'}</td></tr>
<tr><td>統率力</td><td>$in{'tou'}</td>
<td>mail</td><td>$in{'mail'}</td></tr>
</table><p>
初心者向け<form action="$FILE_ENTRY" method="post">
<input type="hidden" name=mode value=RESISDENTS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=num value="0">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="ゲームの説明">
</form><br>
<font size="5" color="red">
初心者さんはこのwiki読むといいかも！<br>
すごいよく出来てる！！<a href="http://www35.atwiki.jp/densetu0net/pages/65.html" target="_blank">伝説の三国志NETwiki-初心者指南</a><br>
</font>
<p>
経験者向け<form action="$FILE_STATUS" method="post">
<input type="hidden" name=mode value=STATUS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="ゲームを開始">
</form></CENTER>
EOM

		&FOOTER;

		exit;
}
1;
