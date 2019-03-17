import nervoussystem.obj.*;

PImage img;
boolean record=false;

void setup(){
  size(480,683,P3D);
  img=loadImage("m51_50.jpg"); 
  img.loadPixels();
  noStroke();
}
void draw(){
  if(record){
    beginRecord("nervoussystem.obj.OBJExport", "m51.obj"); 
  }
  background(255);
  lights();
  translate(width/2,height/2);
  scale(2);
  rotateX(mouseY*.01);
  rotateY(mouseX*.01);
  //image(img,0,0);
  for(int x=0;x<100;x++){
    for(int y=0;y<100;y++){
      int imgx=(int)map(x,0,100,0,img.width);
      int imgy=(int)map(y,0,100,0,img.width);
      float bri=brightness(img.get(imgx,imgy));
       if(bri>100){
        pushMatrix();
        translate(x,y);
        box(bri/90.0);
        popMatrix();
       }
    }
  }
  if(record){
    endRecord();
    record=false;
  }
}
void keyPressed(){
  if(key=='s'||key=='S'){
    record=true;
  } 
}