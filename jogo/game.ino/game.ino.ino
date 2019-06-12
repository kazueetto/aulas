int eixo_X= A0; 
int eixo_Y = A1; 
int botao = 2; 

void setup(){
  pinMode (botao, INPUT_PULLUP); 
  
  Serial.begin (9600); 
}
void loop(){

    if((analogRead(eixo_X)) == 0){ 
        Serial.println("C"); 
    }else{
          if((analogRead(eixo_X)) == 1023){ 
              Serial.println("B"); 
          }else{
                if((analogRead(eixo_Y)) == 0){ 
                  Serial.println("D"); 
                }else{
                      if((analogRead(eixo_Y)) == 1023){ 
                          Serial.println("E"); 
                      }else{
                            if(digitalRead(botao) == LOW){ 
                               Serial.println("P"); 
                            }  
                      }
                }
          }
    }
    delay(500); 
}
