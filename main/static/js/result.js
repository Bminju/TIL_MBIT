$(function(){
    let url = window.location.href;
    let img = $('.result_img img').attr('src');

    $("meta[property='og\\:url']").attr('content', url)
    $("meta[property='og\\:image']").attr('content', img)
});

const copyBtn = document.querySelector('.copy_btn');
const facebookShare = document.querySelector('.facebook_share');


Kakao.API.request({
    url: '/v1/api/talk/friends/message/default/send',
    data: {
      receiver_uuids: ['receiver_uuids'],
      template_object: {
        object_type: 'feed',
        content: {
          title: '카카오톡 링크 4.0',
          description: '디폴트 템플릿 FEED',
          image_url:
            'http://mud-kage.kakao.co.kr/dn/Q2iNx/btqgeRgV54P/VLdBs9cvyn8BJXB3o7N8UK/kakaolink40_original.png',
          link: {
            web_url: 'https://developers.kakao.com',
            mobile_web_url: 'https://developers.kakao.com',
          },
        },
        social: {
          like_count: 100,
          comment_count: 200,
        },
        button_title: '바로 확인',
      },
    },
    success: function(response) {
      console.log(response);
    },
    fail: function(error) {
      console.log(error);
    },
  });

function copyUrl(){
    let tmp = document.createElement('input');
    let url = location.href;

    document.body.appendChild(tmp);
    tmp.value = url;
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);

    alert("URL이 복사되었습니다.");
}

function sharefacebook() {
    let url = window.location.href;
    let facebook = 'http://www.facebook.com/sharer/sharer.php?u=';
    let link = facebook + url;
    window.open(link);
}

copyBtn.addEventListener('click', copyUrl);
facebookShare.addEventListener('click', sharefacebook)
kakaoShare.addEventListener('click', sendLink)