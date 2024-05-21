public class Tester{
  public static void main(String[] args){
    System.out.println(colorByPercent(222, 233));
  }


public static String colorByPercent(int hp, int maxHP){
  String output = String.format("%2s", hp+"")+"/"+String.format("%2s", maxHP+"");
  double percent = (double)hp/maxHP * 100;
  if (percent >= 75){
    output = "\u001B[37m" + output;
  }
  else if(percent < 75 && percent >= 25){
    output = "\u001B[33m" + output;
  }
  else{
    output = "\u001B[31m" + output;
  }
  //COLORIZE THE OUTPUT IF HIGH/LOW:
  // under 25% : red
  // under 75% : yellow
  // otherwise : white
  return output;
}
}
