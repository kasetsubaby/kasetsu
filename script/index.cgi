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
require 'check_com.cgi';

if($MENTE) { &ERR2("スクリプトチェックの為一時的に停止します。"); }
&DECODE;
&INDEX;

#_/_/_/_/_/_/_/_/_/#
#_/  INDEX画面   _/#
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
	while($p<5){$S_MES .= "<font color=008800>●</font>$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$D_MES .= "<font color=000088>●</font>$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$old_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "$LOG_DIR/act_log.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>●</font>$ACT_DATA[$p]<BR>";$p++;}
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
			&MAP_LOG("ゲームプログラムを開始しました。");
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
			unshift(@ACT_DATA,"===============\[$myear年$mmonth月\]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('ファイルを開けませんでした。err no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY データを書き込めません。');
		print OUT @NEW_COU_DATA;
		close(OUT);

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("$mmonth月:<font color=orange>税金</font>で各武将に給与が支払われました。");
			$b_hit = 1;
		}elsif($mmonth eq "7"){
			&MAP_LOG("$mmonth月:<font color=orange>収穫</font>で各武将に米が支払われました。");
			$b_hit = 1;
		}

		# EVENT ACTION
		$eve_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);
		$ihit=0;
		if(!int(rand(40))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<font color=red>【イベント】</font>\[$eve_date\]いなごの大群が畑を襲いました！");
				&MAP_LOG2("<font color=red>【イベント】</font>\[$eve_date\]いなごの大群が畑を襲いました！");
			}elsif($ino eq 1){
				&MAP_LOG("<font color=red>【イベント】</font>\[$eve_date\]洪水がおこりました！各地で被害が出ています！");
				&MAP_LOG2("<font color=red>【イベント】</font>\[$eve_date\]洪水がおこりました！各地で被害が出ています！");
			}elsif($ino eq 2){
				&MAP_LOG("<font color=red>【イベント】</font>\[$eve_date\]疫病が流行っているようです。街の人々も苦しんでいます。。");
				&MAP_LOG2("<font color=red>【イベント】</font>\[$eve_date\]疫病が流行っているようです。街の人々も苦しんでいます。。");
			}elsif($ino eq 3){
				&MAP_LOG("<font color=red>【イベント】</font>\[$eve_date\]今年は豊作になりそうです。");
				&MAP_LOG2("<font color=red>【イベント】</font>\[$eve_date\]今年は豊作になりそうです。");
			}elsif($ino eq 4){
				&MAP_LOG("<font color=red>【イベント】</font>\[$eve_date\]大地震がおこりました！");
				&MAP_LOG2("<font color=red>【イベント】</font>\[$eve_date\]大地震がおこりました！");
			}elsif($ino eq 5){
				&MAP_LOG("<font color=red>【イベント】</font>\[$eve_date\]各町の商店が賑わっています。");
				&MAP_LOG2("<font color=red>【イベント】</font>\[$eve_date\]各町の商店が賑わっています。");
			}
		}
		if($b_hit){
			@NEW_TOWN_DATA=();
			foreach(@TOWN_DATA){
				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/);
				# 相場変動
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

	$MESS1 = "<A href=\"$FILE_CONTNUE\">【CONTNUE】</a>";
	$MESS2 = "<A href=\"$FILE_ENTRY\">【新規登録】</a>";
	&COUNTER;
	$new_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);
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
                        <h1><div style="position:relative;"><s><font color=442200>$GAME_TITLE</font></s></div><div style="margin-bottom:-40px;padding:10px;border:1px solid #999;display:inline-block;position:relative;top:-40px;left:-100px;background:#fff;font-size:12px;transform:rotate(-15deg);">仮設の三国志NET</div></h1>
                        <p><font size=2 color=#9c5a4b></font></p>
                        <p><font size=2 color=#9c5a4b><b>[$new_date]</b><br>
                          次回の更新まで <b>$next_time</b> 分<br>
                          <table bgcolor="#fff">
                            <tbody>
                              <tr>
                                <td>
                                  <font size="2">新規登録（無料）はこちら！→</font><a href="entry.cgi"><b><font size="4">【★新規登録★】</font></b></a><br>
                                  <a href="http://www35.atwiki.jp/densetu0net/pages/65.html" target="_blank">伝説の三国志NETwiki-初心者指南</a><br>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </font></p>
                      </td>
                      <td align="center" bgcolor="#EFE0C0">
                        [<s>携帯用</s>]<br><br><br><br>
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
                                  <b>■ゲーム詳細</b>
                                </td>
                              </tr>
                              <tr>
                                <td bgcolor="#EFE0C0">
                                  <s>【HOME(伝説.NET)】</s><br><br>
                                  <a href="entry.cgi">【新規登録】</a> <br><br>
                                  <a href="ranking.cgi" target="_blank">【登録武将一覧】</a><br> <br>
                                  <a href="manual.html" target="_blank">【説明書】</a> <br><br>
                                  <a href="./map.cgi" target="_blank">【勢力図】</a><br><br>
                                  <a href="./ranking2.cgi" target="_blank">【名将一覧】</a><br><br>
                                  <a href="ranking5.cgi" target="_blank">【統計情報】</a><br><br>
                                  <s>【史記】</s> <br><br>
                                  <a href="https://jbbs.shitaraba.net/bbs/subject.cgi/netgame/16486/" target="_blank">専用ＢＢＳ</a><br><br>
                                  <a href="http://www35.atwiki.jp/densetu0net/" target="_blank">伝説鯖wiki</a><br><br>
                                  <s>三国志NETランキング</s><br><br>
                                  <s>無料ブラウザゲーム</s><br>
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
                                  <b>■お知らせ＆更新履歴</b>
                                </td>
                              </tr>
                              <tr>
                                <td bgcolor="#EFE0C0">
                                  <b>/*２０１４年*/</b><br>
                                  <font size="2">５/２３：<s>来期の改造について</s>。←こんな感じで進めていこうと思います。<br>
                                  </font><br><br>
                                  <font size="3" color="red">７/７：道場で得られる技能の詳細をまとめてみました。遅くなって申し訳なすでした。→ <s>■道場特殊技能の一覧■</s></font><br><br>
                                  <b>/*２０１５年*/</b><br><br><br>
                                  <font size="3" color="red">８/１０：第７４期<b>重要</b>な変更点</font><br>
                                  <table bgcolor="#ffffff">
                                    <tbody>
                                      <tr>
                                        <td>■へんこうてんなど<br><br>
                                          <font color="red" size="5">→<s>７４期改造一覧</s></font><br><br><br>
                                          以前の更新履歴<br>
                                          <a href="kousinnrireki.txt" target="_blank">こちら</a><br>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  ■お知らせ<br><br>
                                  <table bgcolor="#fff">
                                    <tbody>
                                      <tr>
                                        <td>■新着情報！（<a href="./ranking7.cgi" target="_blank">過去ログ</a>）<br>
                                          ・<a href="ranking6.cgi?id=monamona" target="_blank">モナくん</a>がプロフィールを更新しました。 (12日0時0分)<br>
                                          ・<a href="ranking6.cgi?id=erwin" target="_blank">ロンメル将軍</a>がプロフィールを更新しました。 (11日21時17分)<br>
                                          ・<a href="ranking6.cgi?id=monamona" target="_blank">モナくん</a>がプロフィールを更新しました。 (11日19時14分)<br>
                                          ・<a href="ranking6.cgi?id=monamona" target="_blank">モナくん</a>がプロフィールを更新しました。 (9日1時40分)<br>
                                          ・<a href="ranking6.cgi?id=shian" target="_blank">しあーん</a>がプロフィールを更新しました。 (8日19時19分)<br>
                                          ・<a href="ranking6.cgi?id=monamona" target="_blank">モナくん</a>がプロフィールを更新しました。 (8日0時36分)<br>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <font size="4" color="red">１/２５：２月１日２１時頃にリセットを予定しております。よろしくお願いいたします</font><br>
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
                              <td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="ログイン"></td>
                            </tr>
                          </form>
                        </table>
                      </td>
                      <td valign="top">
                        <table bgcolor="#842" align="center" border="0">
                          <tbody>
                            <tr>
                              <td bgcolor="#EFE0C0">
                                現在残り<b>1</b>国<br>
                                現在のログイン人数：<b>2</b>人<br>
                                手紙速度：<b>1401</b>秒（手紙１通につき平均何秒であるか）<br>
                                手紙速度：<b>1</b>通（過去１時間に何通の手紙が行き交ったか）<br>
                                <table bgcolor="#fff">
                                  <tbody>
                                    <tr>
                                      <td>【？】<a href="./manual.html#14" target="_blank">困ったときは</a><br>
                                        <font size="1">・ＩＤ、ＰＷを忘れたとき<br>
                                          ・長期間プレイできない場合の削除停止措置、などなど<br>
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
<input type=submit value=管理者>
</form>

</center>

EOM

	&FOOTER;
	exit;

}
# _/_/_/_/_/_/_/_#
# 即席カウンター #
# _/_/_/_/_/_/_/_#
sub COUNTER {

	$file_read = "$LOG_DIR/counter.cgi";
	open(IN,"$file_read") or &ERR2('ファイルを開けませんでした。');
	@reading = <IN>;
	close(IN);

	($total_count) = split(/<>/,$reading[0]);
	$total_count++;

	&SAVE_DATA("$file_read","$total_count");
}
