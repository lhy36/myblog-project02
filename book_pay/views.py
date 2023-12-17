from django.shortcuts import render, redirect, HttpResponse
import requests
# import json
# from django.template import loader
# from django.http import HttpResponse, JsonResponse

# Create your views here.
def pay(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "0b0173fdc32de47031ed49883752941f",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "german",    # 유저 아이디
            "item_name": "연어초밥",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "12000",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "paySuccess",
            "cancel_url": "payCancel",
            "fail_url": "payFail",
            "tid": request.session['tid'],
        }
        res = requests.post(URL, headers=headers, params=params)
        print(res.json())
        try:
            request.session['tid'] = res.json()['tid']
            next_url = res.json()['next_redirect_pc_url']
            return redirect(next_url)
        except KeyError as e:
        # KeyError 예외 처리
            print(f"KeyError: {e}")
            # 또는 다른 대체 동작을 정의
        return HttpResponse("알 수 없는 오류가 발생했습니다.")

    return render(request, 'pay.html')

def approval(request):
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "0b0173fdc32de47031ed49883752941f",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",     # 주문번호
        "partner_user_id": "german",    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'kakaopay/approval.html', context)
def kakaoPay(request):
    return render(request, 'kakaopay.html')

def kakaoPayLogic(request):
    _admin_key = '0b0173fdc32de47031ed49883752941f' # 입력필요
    _url = f'https://kapi.kakao.com/v1/payment/ready'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
    }
    _data = {
        'cid': 'TC0ONETIME',
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'item_name':'책',
        'quantity':'1',
        'total_amount':'22000',
        'tax_free_amount':'0',
        # 내 애플리케이션 -> 앱설정 / 플랫폼 - WEB 사이트 도메인에 등록된 정보만 가능합니다
        # * 등록 : http://IP:8000 
        'approval_url':'http://127.0.0.1:8000/pay/paySuccess', 
        'fail_url':'http://127.0.0.1:8000/pay/payFail',
        'cancel_url':'http://127.0.0.1:8000/pay/payCancel'
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    request.session['tid'] = _result['tid']
    return redirect(_result['next_redirect_pc_url'])

def paySuccess(request):
    _url = 'https://kapi.kakao.com/v1/payment/approve'
    _admin_key = '0b0173fdc32de47031ed49883752941f' # 입력필요
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
    _data = {
        'cid':'TC0ONETIME',
        'tid': request.session['tid'],
        'amount':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'pg_token': request.GET['pg_token']
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    if _result.get('msg'):
        return redirect('/payFail')
    else:
        # * 사용하는 프레임워크별 코드를 수정하여 배포하는 방법도 있지만
        #   Req Header를 통해 분기하는 것을 추천
        # - Django 등 적용 시
        # return render(request, 'paySuccess.html')
        print(_result)
        # - React 적용 시
        return redirect('http://localhost:3000')
    
def kakaoLoginLogic(request):
    _restApiKey = 'd5b26dd6d83ae5397a776595b1468fd9' # 입력필요
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = 'd5b26dd6d83ae5397a776595b1468fd9' # 입력필요
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'loginSuccess.html')

def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    # _url = 'https://kapi.kakao.com/v1/user/unlink'
    # _header = {
    #   'Authorization': f'bearer {_token}',
    # }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'loginoutSuccess.html')
    else:
        return render(request, 'logoutError.html')
    
def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')