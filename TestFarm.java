
import AnimalsPackage.*;
import FarmPackage.*;

public class TestFarm {
	public static void main(String[] args) {
		
		Farm myFarm = new Farm();
		
		Cow c = new Cow(100, "grass");
		Hen h = new Hen(2, "seeds");
		Dog d = new Dog(5, "bones");
		
		myFarm.addDomesticated(c);
		myFarm.addDomesticated(h);
	  //myFarm.addDomesticated(d);
	  //the addDomesticated parameters are for domesticated animals only 
		
		myFarm.allFeed();
		myFarm.allFeed();
		
		myFarm.allYield();
		
		myFarm.allFeed();
		myFarm.allFeed();
		myFarm.allFeed();
		myFarm.allFeed();
		myFarm.allFeed();
		
		myFarm.allYield();

		
	}

}
