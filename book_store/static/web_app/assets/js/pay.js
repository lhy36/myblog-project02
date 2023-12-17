// your_stripe_payment_script.js

// Stripe Publishable Key 설정
var stripe = Stripe('your_publishable_key');

// Stripe Elements 초기화
var elements = stripe.elements();
var cardElement = elements.create('card');
cardElement.mount('#card-element');

// 폼 제출 시에 Stripe.js를 통해 토큰을 생성하고 폼에 추가
var form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.createToken(cardElement).then(function(result) {
        if (result.error) {
            // 카드 정보가 유효하지 않을 때 오류 메시지를 표시
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // 토큰을 폼에 추가하고 폼 다시 제출
            var hiddenInput = document.createElement('input');
            hiddenInput.setAttribute('type', 'hidden');
            hiddenInput.setAttribute('name', 'stripeToken');
            hiddenInput.setAttribute('value', result.token.id);
            form.appendChild(hiddenInput);
            form.submit();
        }
    });
});
