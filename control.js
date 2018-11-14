let first = ""
let list: string[] = []
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    list = [bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))]
    first = list.shift()
    if (first == "w") {
        basic.showString("w")
        pins.servoWritePin(AnalogPin.P0, 180)
        pins.servoWritePin(AnalogPin.P1, 0)
    } else if (first == "s") {
        basic.showString("s")
        pins.servoWritePin(AnalogPin.P0, 90)
        pins.servoWritePin(AnalogPin.P1, 90)
    } else if (first == "a") {
        basic.showString("a")
        pins.servoWritePin(AnalogPin.P0, 180)
        pins.servoWritePin(AnalogPin.P1, 90)
    } else if (first == "d") {
        basic.showString("d")
        pins.servoWritePin(AnalogPin.P0, 90)
        pins.servoWritePin(AnalogPin.P1, 0)
    }
})
bluetooth.startUartService()
bluetooth.advertiseUid(
0,
0,
7,
true
)

