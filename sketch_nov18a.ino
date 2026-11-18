#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();
    lcd.backlight();
    Serial.begin(9600);

    lcd.print("Aguardando...");
}

void loop() {
    if (Serial.available() > 0) {
        String mensagem = Serial.readStringUntil('\n');
        mensagem.trim();

        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("OS atual:");

        lcd.setCursor(0, 1);
        lcd.print(mensagem);
    }
}