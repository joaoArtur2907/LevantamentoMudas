 const b2b = document.getElementsByClassName('b2b')[0]
  let b2c = document.getElementsByClassName('b2c')[0]

  function porcentageB2B() {
    let valueB2B = document.querySelector('.b2b').value
    let valueB2C = document.querySelector('.b2c').value

    let valueMissing = valueB2B - 100
    positiveValueMissing = Math.abs(valueMissing)
    console.log(positiveValueMissing)

    if(positiveValueMissing <= 100) {
        b2c.value = positiveValueMissing
    } else {
        b2c.value = 100
    }
  }

  function porcentageB2C() {
    let valueB2B = document.querySelector('.b2b').value
    let valueB2C = document.querySelector('.b2c').value

    let valueMissing = valueB2C - 100
    positiveValueMissing = Math.abs(valueMissing)
    console.log(positiveValueMissing)

    if(positiveValueMissing <= 100) {
        b2b.value = positiveValueMissing
    } else {
        b2b.value = 100
    }
  }

  b2b.addEventListener('input', porcentageB2B);
  b2c.addEventListener('input', porcentageB2C);