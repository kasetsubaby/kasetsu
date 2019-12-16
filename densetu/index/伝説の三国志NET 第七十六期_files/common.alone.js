var error = {
  eParam: {
    bidimpid: kit.getParam($wrapper, 'bidimpid'),
    adid: kit.getParam($wrapper, 'adid'),
    width: kit.getParam($wrapper, 'width'),
    height: kit.getParam($wrapper, 'height'),
    adx: kit.getParam($wrapper, 'adx'),
    bid_utc_time: kit.getParam($wrapper, 'bid_utc_time'),
    domain_us: kit.getParam($wrapper, 'track_hosts'),
    preview: kit.getParam($wrapper, 'preview')
      ? kit.getParam($wrapper, 'preview')
      : '',
  },
  eNode: '',
  eFunc: function() {
    var e = this,
      t = document.createElement('iframe');
    (t.style.display = 'none'),
      document.getElementById('rtb-suggested-link').appendChild(t),
      (t.src =
        e.eParam.domain_us +
        '/yh/error?bidimpid=' +
        e.eParam.bidimpid +
        '&adid=' +
        e.eParam.adid +
        '&ym-width=' +
        e.eParam.width +
        '&ym-height=' +
        e.eParam.height +
        '&adx=' +
        e.eParam.adx +
        '&bid_utc_time=' +
        e.eParam.bid_utc_time +
        '&rtbImpType=banner'),
      (e.eNode = t);
  },
};
try {
  kit.randomPic();
} catch (e) {
  'false' == error.eParam.preview &&
    (error.eFunc(), (error.eNode.src += '&msg=' + e.message));
}
var base = {
  width: kit.getParam($wrapper, 'width'),
  height: kit.getParam($wrapper, 'height'),
  getRan: kit.randomPic(),
  useIdArr: [],
};

function addParameterToURL(_url,param){
    _url += (_url.split('?')[1] ? '&':'?') + param;
    return _url;
}

($wrapper.style.width = base.width + 'px'),
  ($wrapper.style.height = base.height + 'px');
var func = {
  chooseImg: function() {
    if (
      kit.getByClass(document, 'rtb-suggested-main-img').length > 0 &&
      kit.getByClass(document, 'img').length > 0
    ) {
      var e = kit.getByClass(document, 'img')[0].clientWidth,
        t = kit.getByClass(document, 'img')[0].clientHeight,
        a = e / t;
      if ($wrapper.getAttribute('feed_params'))
        var r = JSON.parse(
          decodeURIComponent($wrapper.getAttribute('feed_params'))
        );
      else
        var r = JSON.parse(
          decodeURIComponent($wrapper.getAttribute('linkData'))
        );
      for (var i = [], p = [], d = 0; d < r.length; d++)
        if ($wrapper.getAttribute('feed_params'))
          if (r[d].Image_link.indexOf('?width=') > -1) {
            var m = r[d].Image_link.split('?')[1]
                .split('&')[0]
                .split('=')[1],
              n = r[d].Image_link.split('?')[1]
                .split('&')[1]
                .split('=')[1],
              g = m / n;
            i.push(g - a);
          } else '' == r[d].Image_link ? i.push(999) : i.push(998);
        else if (r[d].ImageUrl.indexOf('?width=') > -1) {
          var m = r[d].ImageUrl.split('?')[1]
              .split('&')[0]
              .split('=')[1],
            n = r[d].ImageUrl.split('?')[1]
              .split('&')[1]
              .split('=')[1],
            g = m / n;
          i.push(g - a);
        } else '' == r[d].ImageUrl ? i.push(999) : i.push(998);
      for (var s = Math.min.apply(null, i), d = 0; d < i.length; d++)
        i[d] == s && p.push(d);
      return p[Math.floor(Math.random() * p.length)];
    }
    return base.getRan;
  },
  arrUnique: function(e) {
    for (var t = [], a = {}, r = 0; r < e.length; r++)
      a[e[r]] || (t.push(e[r]), (a[e[r]] = 1));
    return t;
  },
  getFeedId: function() {
    if ($wrapper.getAttribute('feed_params')) {
      for (
        var e = JSON.parse(
            decodeURIComponent($wrapper.getAttribute('feed_params'))
          ),
          t = 0;
        t < e.length;
        t++
      )
        ('' != e[t].image_link && '' != e[t].Image_link) ||
          (e.splice(t, 1), t--);
      for (var t = 0; t < e.length; t++) base.useIdArr.push(e[t].Id);
    } else {
      for (
        var e = JSON.parse(
            decodeURIComponent($wrapper.getAttribute('linkData'))
          ),
          t = 0;
        t < e.length;
        t++
      )
        ('' != e[t].imageUrl && '' != e[t].ImageUrl) || (e.splice(t, 1), t--);
      for (var t = 0; t < e.length; t++) base.useIdArr.push(e[t].ImageId);
    }
  },
};
setTimeout(function() {
  var e = { getChooseImg: func.chooseImg() };
  ({
    init: function() {
      var e = this;
      e.multiPic(), e.gifJumpTo(), e.event();
    },
    event: function() {
      var e = this,
        t = kit.getByClass(document, 'rtb-suggested-main-img');
      if (t.length > 0) {
        for (var a = 0; a < t.length; a++) t[a].src = this.param.picture;
        this.jumpTo();
      }
      'false' == e.param.preview && (new Image(1, 1).src = this.flash());
    },
    param: {
      width: kit.getParam($wrapper, 'width'),
      height: kit.getParam($wrapper, 'height'),
      bidimpid: kit.getParam($wrapper, 'bidimpid'),
      adid: kit.getParam($wrapper, 'adid'),
      adx: kit.getParam($wrapper, 'adx'),
      req_id: kit.getParam($wrapper, 'req_id'),
      domain_us: kit.getParam($wrapper, 'track_hosts'),
      id: kit.getFeed($wrapper, e.getChooseImg, 'imageId')
        ? kit.getFeed($wrapper, e.getChooseImg, 'imageId')
        : kit.getFeed($wrapper, e.getChooseImg, 'id'),
      link: kit.getFeed($wrapper, e.getChooseImg, 'targetLink')
        ? kit.getFeed($wrapper, e.getChooseImg, 'targetLink')
        : kit.getFeed($wrapper, e.getChooseImg, 'link'),
      picture: kit.getFeed($wrapper, e.getChooseImg, 'image_link')
        ? kit.getFeed($wrapper, e.getChooseImg, 'image_link')
        : kit.getFeed($wrapper, e.getChooseImg, 'imageUrl'),
      mkPixelId: kit.getParam($wrapper, 'mkPixelId'),
      nc: kit.getParam($wrapper, 'nc'),
      preview: kit.getParam($wrapper, 'preview')
        ? kit.getParam($wrapper, 'preview')
        : '',
      urltags: kit.getParam($wrapper, 'urltags')
        ? kit.getParam($wrapper, 'urltags')
        : 'utm_source=YM&utm_medium=RM&utm_content=ym-krtb_3047c633rds2ac8cf45d5a79735324d6qwea62er621a&utm_term=20190432MK&utm_campaign=mk',
      curltags: kit.getParam($wrapper, 'curltags')
        ? kit.getParam($wrapper, 'curltags')
        : 'utm_source=YM&utm_medium=RM&utm_content=ym-krtb_3047c633rds2ac8cf45d5a79735324d6qwea62er621a&utm_term=20190432MK&utm_campaign=mk',
      turltags: kit.getParam($wrapper, 'turltags')
        ? kit.getParam($wrapper, 'turltags')
        : '',
    },
    imglink: function() {
      var e = this;
      return $wrapper.getAttribute('feed_params')
        ? e.param.domain_us +
            '/yh/click?adid=' +
            e.param.adid +
            '&bidimpid=' +
            e.param.bidimpid +
            '&adx=' +
            e.param.adx +
            '&req_id=' +
            e.param.req_id +
            '&clickContentId=' +
            e.param.id +
            '&tracker=' +
            encodeURIComponent(addParameterToURL(e.param.link,e.param.curltags)+'&bidimpid='+(e.param.bidimpid||'9999999999999999999999')) +
            '&mkPixelId=' +
            e.param.mkPixelId
        : e.param.domain_us +
            '/yh/click?adid=' +
            e.param.adid +
            '&bidimpid=' +
            e.param.bidimpid +
            '&adx=' +
            e.param.adx +
            '&req_id=' +
            e.param.req_id +
            '&imgId=' +
            e.param.id +
            '&tracker=' +
            encodeURIComponent(addParameterToURL(e.param.link, e.param.curltags)+'&bidimpid='+(e.param.bidimpid||'9999999999999999999999')) +
            '&mkPixelId=' +
            e.param.mkPixelId;
    },
    getData: function(e, t) {
      if (void 0 == e[t]) {
        var a = t.split(''),
          r = '';
        return (a[0] = a[0].toUpperCase()), (r = a.join('')), e[r];
      }
      return e[t];
    },
    flash: function() {
      var e = this,
        t = kit.flashChecker();
      void 0 != e.param.nc && '' != e.param.nc && e.param.nc,
        (e.param.bidimpid && '' != e.param.bidimpid) ||
          'false' != e.param.preview ||
          (error.eFunc(), (error.eNode.src += '&msg=bidimpid is none'));
      var a =
        e.param.domain_us +
        '/yh/impression?bidimpid=' +
        e.param.bidimpid +
        '&adid=' +
        e.param.adid +
        '&req_id=' +
        e.param.req_id +
        '&vertion=v_20190403&' +
        e.param.urltags;
      0 != t.f ? (a += '&flash=1&fvertion=' + t.v) : (a += '&flash=0'),
        (document.getElementById('gif-single-one') ||
          document.getElementById('gif-multi-wrapper')) &&
          func.getFeedId();
      var r = func.arrUnique(base.useIdArr),
        i = r.join('__');
      return (
        kit.getByClass(document, 'rtb-suggested-main-img').length > 0
          ? $wrapper.getAttribute('feed_params')
            ? (a += '&imp_feed_ids=' + e.param.id)
            : (a += '&imp_img_ids=' + e.param.id)
          : $wrapper.getAttribute('feed_params')
          ? (a += '&imp_feed_ids=' + i)
          : (a += '&imp_img_ids=' + i),
        a
      );
    },
    jumpTo: function() {
      var e = this,
        t = document.getElementById('rtb-suggested-link'),
        a = document.createElement('a');
      a.setAttribute('target', '_blank'),
        a.appendChild(t),
        document.getElementById('inner-div').appendChild(a),
        a.addEventListener(
          'click',
          function(t) {
            var r =
              e.imglink() +
              '&clickX=' +
              t.clientX +
              '&clickY=' +
              t.clientY +
              '&screenX=' +
              t.screenX +
              '&screenY=' +
              t.screenY +
              '&pageX=' +
              t.pageX +
              '&pageY=' +
              t.pageY +
              '&offsetX=' +
              t.offsetX +
              '&offsetY=' +
              t.offsetY +
              '&wHref=' +
              encodeURIComponent(window.location.href);
            a.setAttribute('href', r);
          },
          !1
        );
    },
    multiPic: function() {
      var e = this,
        t = document.getElementById('img-wrapper');
      if (t) {
        if (kit.getByClass(document, 'multiImg').length > 0)
          var a = kit.getByClass(document, 'multiImg');
        else var a = t.getElementsByTagName('img');
        var r = t.getElementsByTagName('a');
        if ($wrapper.getAttribute('feed_params'))
          var i = JSON.parse(
            decodeURIComponent($wrapper.getAttribute('feed_params'))
          );
        else
          var i = JSON.parse(
            decodeURIComponent($wrapper.getAttribute('linkData'))
          );
        for (var p = i, d = 0; d < i.length; d++)
          $wrapper.getAttribute('feed_params')
            ? ('' != i[d].image_link && '' != i[d].Image_link) ||
              (i.splice(d, 1), d--)
            : ('' != i[d].imageUrl && '' != i[d].ImageUrl) ||
              (i.splice(d, 1), d--);
        if (i.length >= a.length) p = i.slice(0, a.length);
        else
          for (var m = 0, n = i.length, g = 0; g < a.length - n; g++)
            (m > n - 1 || 1 == n) && (m = 0), p.push(i[m]), m++;
        for (var d = 0; d < a.length; d++)
          $wrapper.getAttribute('feed_params')
            ? (r[d].setAttribute(
                'data-href',
                e.param.domain_us +
                  '/yh/click?adid=' +
                  e.param.adid +
                  '&bidimpid=' +
                  e.param.bidimpid +
                  '&adx=' +
                  e.param.adx +
                  '&req_id=' +
                  e.param.req_id +
                  '&clickContentId=' +
                  e.getData(p[d], 'id') +
                  '&tracker=' +
                  encodeURIComponent(addParameterToURL(e.getData(p[d], 'link'),e.param.curltags)+'&bidimpid='+(e.param.bidimpid||'9999999999999999999999')) +
                  '&mkPixelId=' +
                  e.param.mkPixelId
              ),
              (a[d].src = p[d].image_link || p[d].Image_link),
              base.useIdArr.push(e.getData(p[d], 'id')))
            : (r[d].setAttribute(
                'data-href',
                e.param.domain_us +
                  '/yh/click?adid=' +
                  e.param.adid +
                  '&bidimpid=' +
                  e.param.bidimpid +
                  '&adx=' +
                  e.param.adx +
                  '&req_id=' +
                  e.param.req_id +
                  '&imgId=' +
                  e.getData(p[d], 'imageId') +
                  '&tracker=' +
                  encodeURIComponent(addParameterToURL(e.getData(p[d], 'targetLink'),e.param.curltags)+'&bidimpid='+(e.param.bidimpid||'9999999999999999999999')) +
                  '&mkPixelId=' +
                  e.param.mkPixelId
              ),
              (a[d].src = p[d].imageUrl || p[d].ImageUrl),
              base.useIdArr.push(e.getData(p[d], 'imageId')));
        this.multiJumpTo();
      }
    },
    multiJumpTo: function() {
      var e = document.getElementById('rtb-suggested-link'),
        t = document.getElementById('img-wrapper'),
        a = t.getElementsByTagName('a'),
        r = document.createElement('a');
      r.setAttribute('target', '_blank'),
        r.appendChild(e),
        document.getElementById('inner-div').appendChild(r);
      for (
        var i = function(e, t) {
            var i;
            if ('as' == t)
              (i = e.path[1].getAttribute('data-href')),
                (i +=
                  '&clickX=' +
                  e.clientX +
                  '&clickY=' +
                  e.clientY +
                  '&screenX=' +
                  e.screenX +
                  '&screenY=' +
                  e.screenY +
                  '&pageX=' +
                  e.pageX +
                  '&pageY=' +
                  e.pageY +
                  '&offsetX=' +
                  e.offsetX +
                  '&offsetY=' +
                  e.offsetY +
                  '&wHref=' +
                  encodeURIComponent(window.location.href)),
                e.path[1].setAttribute('target', '_blank'),
                e.path[1].setAttribute('href', i),
                e.stopPropagation();
            else {
              var p = Math.floor(Math.random() * a.length);
              (i = a[p].getAttribute('data-href')),
                (i +=
                  '&clickX=' +
                  e.clientX +
                  '&clickY=' +
                  e.clientY +
                  '&screenX=' +
                  e.screenX +
                  '&screenY=' +
                  e.screenY +
                  '&pageX=' +
                  e.pageX +
                  '&pageY=' +
                  e.pageY +
                  '&offsetX=' +
                  e.offsetX +
                  '&offsetY=' +
                  e.offsetY +
                  '&wHref=' +
                  encodeURIComponent(window.location.href)),
                r.setAttribute('href', i);
            }
          },
          p = 0;
        p < a.length;
        p++
      )
        a[p].addEventListener(
          'click',
          function() {
            i(event, 'as');
          },
          !1
        );
      $wrapper.addEventListener(
        'click',
        function() {
          i(event, 'wrapper');
        },
        !1
      );
    },
    gifJumpTo: function() {
      if (document.getElementById('gif-single-one')) {
        var e = this,
          t = document.getElementById('gif-wrapper');
        t.setAttribute('target', '_blank');
        var a = function(a) {
          var r = t.getAttribute('data-href');
          t.setAttribute(
            'data-href',
            r +
              '&adid=' +
              e.param.adid +
              '&bidimpid=' +
              e.param.bidimpid +
              '&adx=' +
              e.param.adx +
              '&req_id=' +
              e.param.req_id +
              '&mkPixelId=' +
              e.param.mkPixelId +
              '&' +
              e.param.curltags
          );
          var i =
            t.getAttribute('data-href') +
            '&clickX=' +
            a.clientX +
            '&clickY=' +
            a.clientY +
            '&screenX=' +
            a.screenX +
            '&screenY=' +
            a.screenY +
            '&pageX=' +
            a.pageX +
            '&pageY=' +
            a.pageY +
            '&offsetX=' +
            a.offsetX +
            '&offsetY=' +
            a.offsetY +
            '&wHref=' +
            encodeURIComponent(window.location.href);
          t.setAttribute('href', i);
        };
        t.addEventListener('click', a, !1);
      }
      if (document.getElementById('gif-multi-wrapper'))
        for (
          var e = this,
            t = document.getElementById('gif-multi-wrapper'),
            r = t.getElementsByTagName('a'),
            a = function(t) {
              var a = this.getAttribute('data-href');
              this.setAttribute(
                'data-href',
                a +
                  '&adid=' +
                  e.param.adid +
                  '&bidimpid=' +
                  e.param.bidimpid +
                  '&adx=' +
                  e.param.adx +
                  '&req_id=' +
                  e.param.req_id +
                  '&mkPixelId=' +
                  e.param.mkPixelId +
                  '&' +
                  e.param.curltags
              );
              var r =
                this.getAttribute('data-href') +
                '&clickX=' +
                t.clientX +
                '&clickY=' +
                t.clientY +
                '&screenX=' +
                t.screenX +
                '&screenY=' +
                t.screenY +
                '&pageX=' +
                t.pageX +
                '&pageY=' +
                t.pageY +
                '&offsetX=' +
                t.offsetX +
                '&offsetY=' +
                t.offsetY +
                '&wHref=' +
                encodeURIComponent(window.location.href);
              t.path[1].setAttribute('target', '_blank'),
                t.path[1].setAttribute('href', r);
            },
            i = 0;
          i < r.length;
          i++
        )
          r[i].addEventListener('click', a, !1);
    },
  }.init());
}, 600);

