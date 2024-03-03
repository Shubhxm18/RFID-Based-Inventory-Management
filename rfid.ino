#include <SPI.h>
#include <MFRC522.h>

constexpr uint8_t RST_PIN = D3;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = D4;     // Con hfigurable, see typical pin layout above

MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class
MFRC522::MIFARE_Key key;

String tag;
int tagCounter[4] = {0}; // Counter array for each RFID tag

struct RFIDInfo {
  String tag;
  String name;
};

RFIDInfo rfidTags[] = {
  {"221222184137", "ATTITUDE IS EVERYTHING"},
  {"2699123118", "THE POWER OF YOUR SUBCONSCIOUS MIND"},
  // Add more RFID tags and names as needed
  {"1533103104", "THE SECRET"},
  {"153224204104", "THINKING STATE"}
};

void setup() {
  Serial.begin(9600);
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522
  pinMode(D8, OUTPUT);
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent())
    return;

  if (rfid.PICC_ReadCardSerial()) {
    for (byte i = 0; i < 4; i++) {
      tag += rfid.uid.uidByte[i];
    }

    Serial.println(tag);

    for (int i = 0; i < sizeof(rfidTags) / sizeof(rfidTags[0]); i++) {
      if (tag == rfidTags[i].tag) {
        digitalWrite(D8, HIGH);
        delay(100);
        digitalWrite(D8, LOW);

        Serial.print(rfidTags[i].name);

        if (tagCounter[i] == 0) {
          Serial.println(" ISSUED");
        } else if (tagCounter[i] == 1) {
          Serial.println(" RETURN");
        }

        // Reset the counter after every successful scan
        tagCounter[i] = (tagCounter[i] + 1) % 2;
      }
    }

    if (tag != rfidTags[0].tag && tag != rfidTags[1].tag && tag != rfidTags[2].tag && tag != rfidTags[3].tag) {
      Serial.println("THIS BOOK IS NOT VALID");
      digitalWrite(D8, HIGH);
      delay(2000);
      digitalWrite(D8, LOW);
    }

    tag = "";
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();
  }
}
