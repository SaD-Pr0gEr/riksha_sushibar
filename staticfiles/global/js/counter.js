let counterClasses = [
    {
        className: 'product',
        counter: 1,
    },
    {
        className: 'product-detail-order',
        counter: 1,
    }
]

counterClasses.forEach((value) => {
    let counter = document.querySelector('.counter' + `.${value['className']}`);
    counter.querySelector('.counter-value').innerHTML = value['counter']
    counter.querySelector('.decrement').addEventListener(
        'click', () => {
            let newDecrement = value['counter'] - 1
            if (newDecrement >= 0) {
                value['counter'] = newDecrement
                counter.querySelector('.counter-value').innerHTML = value['counter']
            }
            let check = document.querySelector('.instant-order-sum span')
            if (check) {
                let sumValue = document.querySelector('.product-instant-order-item.product-price span')
                check.innerHTML = String(value['counter'] * Number(sumValue.innerHTML))
                document.querySelector('#instant_order input[name="product_count"]').value = value['counter']
            }
        }
    )
    counter.querySelector('.increment').addEventListener(
        'click', () => {
            let newValue = value['counter'] + 1
            if (newValue >= 0) {
                value['counter'] = newValue
                counter.querySelector('.counter-value').innerHTML = value['counter']
            }
            let check2 = document.querySelector('.instant-order-sum span')
            if (check2) {
                let sumValue2 = document.querySelector('.product-instant-order-item.product-price span')
                check2.innerHTML = String(value['counter'] * Number(sumValue2.innerHTML))
                document.querySelector('#instant_order input[name="product_count"]').value = value['counter']
            }
        }
    )
})
