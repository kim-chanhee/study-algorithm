// # 2차원 배열과 for문 활용 숫자 순차적 반복 수행
const unsigned int led[7] = {2,3,4,5,6,7,8};

const unsigned int num[2][7]= {
    {1,1,1,1,1,1,0}
    {0,1,1,0,0,0,0}
}

void display_int(){
    for(int x=0;x<7;x++){
        pinMode(led[x], OUTPUT);
    }
}

void display_clear(){
    for(int x=0; x<7; x++){
        digitalWrite(led[x], LOW);
    }
}

void display_number(int n){
    if(0<=n&&n<=1){
       for(int x=0; x<7; x++){
           digitalWrite(led[x], num[n][x]==1?HIGH:LOW);
       }
    }
}

void setup(){
    diplay_init();
}
void loop(){
    for(int n=0;n<=1;n++){
        display_clear();
        display_number(n);
        delay(500);
    }
}
// #-------------------------------
// # 7 세그먼트 켜고 꺼보기
const unsigned int led[7] = {2,3,4,5,6,7,8};

void setup(){
    for(int x=0; x<7; x++){
        pinMode(led[x], OUTPUT);
    }
}

void loop(){
    // # led 켜기
    for(int x=0;x<7;x++){
        digitalWrite(led[x], HIGH);
    }
    delay(500);

    // # led 끄기
    for(int x=0; x<7; x++){
        digitalWirte(led[x], LOW);
    }
    delay(500);
}
// #=================
// # led 차례대로 켜고 꺼보기
const unsigned int led[7] = {2,3,4,5,6,7,8};

void setup(){
    for(int x=0; x<7; x++){
        pinMode(led[x], OUTPUT);
    }
}

void loop(){
    for(int x=0; x<7; x++){
        
        // # led 모두 끄기
        for(int x=0; x<7; x++){
            digitalWrite(led[x], LOW);
        }

        digitalWrite(led[x], HIGH);

        delay(500);
    }
}
// 움직이는 공
enum { R5=1, R7, C2, C3, R8, C5,R6, R3, R1, C4, C6, R4, C1, R2, C7, C8}
const unsigned int pins[1+16]= {
    -1,1011121314151617 234566789
}

const unsigned int R[1+8]
const unsigned int C[1+8]

unsigned int game_display