package FarmPackage;
import java.util.ArrayList;
import java.util.List;

import AnimalsPackage.Domesticated;

public class Farm {

	List<Domesticated> animals = new ArrayList<Domesticated>();
	
	public Farm() {
	}
	
	public void addDomesticated(Domesticated animal) {
		animals.add(animal);
	}
	
	public void allFeed() {
		for (Domesticated x : animals) {
			x.feed();
		}
	}
	
	public void allYield() {
		for (Domesticated x: animals) {
			x.yield();
		}
		
	}
	
}
