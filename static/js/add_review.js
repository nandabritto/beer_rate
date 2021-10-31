// get all the stars
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.review-form')


const handleSelect = (selection) => {
    switch (selection) {
        case 'first'|| 'cheap': {
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return

        }
        case 'second': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return

        }
        case 'third': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return

        }
        case 'fourth': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            return

        }
        case 'fifth': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            return

        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } else if (stringValue === 'second') {
        numericValue = 2
    } else if (stringValue === 'third') {
        numericValue = 3
    } else if (stringValue === 'fourth') {
        numericValue = 4
    } else if (stringValue === 'fifth') {
        numericValue = 5
    } else {
        numericValue = 0
    }
    return numericValue
}


const arr = [one, two, three, four, five]

arr.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelect(event.target.id)

}))


arr.forEach(item => item.addEventListener('click', (event) => {
    // value of the rating not numeric
    const val = event.target.id
    console.log(val)

    const val_num = getNumericValue(val)
    console.log(val_num)
    form.score.value = val_num
    console.log(form.score.value)
}))