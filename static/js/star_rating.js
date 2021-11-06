// console.log(score)
// const one = document.getElementById('one')
// const two = document.getElementById('two')
// const three = document.getElementById('three')
// const four = document.getElementById('four')
// const five = document.getElementById('five')


// // get the hover stars and add/remove checked class
// if (score == 0) {
//         one.classList.remove('checked')
//         two.classList.remove('checked')
//         three.classList.remove('checked')
//         four.classList.remove('checked')
//         five.classList.remove('checked')
// }
// if (score == 1) {
//         one.classList.add('checked')
//         two.classList.remove('checked')
//         three.classList.remove('checked')
//         four.classList.remove('checked')
//         five.classList.remove('checked')
// }
// if (score == 2) {
//         one.classList.add('checked')
//         two.classList.add('checked')
//         three.classList.remove('checked')
//         four.classList.remove('checked')
//         five.classList.remove('checked')
// }

//         }
//         case 'second': {
//             one.classList.add('checked')
//             two.classList.add('checked')
//             three.classList.remove('checked')
//             four.classList.remove('checked')
//             five.classList.remove('checked')
//             return

//         }
//         case 'third': {
//             one.classList.add('checked')
//             two.classList.add('checked')
//             three.classList.add('checked')
//             four.classList.remove('checked')
//             five.classList.remove('checked')
//             return

//         }
//         case 'fourth': {
//             one.classList.add('checked')
//             two.classList.add('checked')
//             three.classList.add('checked')
//             four.classList.add('checked')
//             five.classList.remove('checked')
//             return

//         }
//         case 'fifth': {
//             one.classList.add('checked')
//             two.classList.add('checked')
//             three.classList.add('checked')
//             four.classList.add('checked')
//             five.classList.add('checked')
//             return

//         }
//     }
// }

// ///Get string value from stars and add numeric value 
// const getNumericValue = (stringValue) => {
//     let numericValue;
//     if (stringValue === 'first') {
//         numericValue = 1
//     } else if (stringValue === 'second') {
//         numericValue = 2
//     } else if (stringValue === 'third') {
//         numericValue = 3
//     } else if (stringValue === 'fourth') {
//         numericValue = 4
//     } else if (stringValue === 'fifth') {
//         numericValue = 5
//     } else {
//         numericValue = 0
//     }
//     return numericValue
// }


// const arr = [one, two, three, four, five]

// ///Add event listener to mouse hover on rating stars
// arr.forEach(item => item.addEventListener('mouseover', (event) => {
//     handleSelect(event.target.id)

// }))

// /// Tranform string value from stars into numeric value 
// arr.forEach(item => item.addEventListener('click', (event) => {
//     const val = event.target.id
//     const val_num = getNumericValue(val)
//     form.score.value = val_num
// }))