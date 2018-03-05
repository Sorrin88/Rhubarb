package FarmPackage;

import AnimalsPackage.Animal;
import AnimalsPackage.Domesticated;

public class Hen extends Animal implements Domesticated {

	int foodCount;

	public Hen(double weight, String food) {
		super(weight);
		this.addFood(food);
	}

	@Override
	public void feed() {
		System.out.println("The hen enjoyed her seeds.");
		foodCount++;
	}

	@Override
	public void yield() {
		if (foodCount > 3) {
			System.out.println("The hen laid an egg.");
			foodCount = 0;
		} else {
			System.out.println("The hen did not lay eggs and has only had " + foodCount + " meals.");
		}
	}

	@Override
	public void makeSound() {
		// TODO Auto-generated method stub

	}

}
