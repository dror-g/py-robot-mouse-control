let counter = false
let right = 0
let power = 0
let list: string[] = []
let left = 0
// pins.servoWritePin(AnalogPin.P0, 180)
// pins.servoWritePin(AnalogPin.P1, 0)
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    list = [bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))]
    // right = right + parseInt(list.shift()) left = left
    // left = left - parseInt(list.shift())
    power = parseInt(list.shift())
    if (counter == false) {
        right = power
        pins.servoWritePin(AnalogPin.P0, right)
        counter = true
    } else {
        left = power
        pins.servoWritePin(AnalogPin.P1, left)
        counter = false
    }
})
left = 90
right = 90
bluetooth.startUartService()
bluetooth.advertiseUid(
0,
0,
7,
true
)

