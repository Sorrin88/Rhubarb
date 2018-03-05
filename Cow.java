package FarmPackage;

import AnimalsPackage.Animal;
import AnimalsPackage.Domesticated;

public class Cow extends Animal implements Domesticated {

	int foodCount;

	public Cow(double weight, String food) {
		super(weight);
		this.addFood(food);
	}

	@Override
	public void feed() {
		System.out.println("The cow enjoyed her hay and grains.");
		foodCount++;
	}

	@Override
	public void yield() {
		if (foodCount > 3) {
			System.out.println("The cow gave milk.");
			foodCount = 0;
		} else {
			System.out.println("The cow did not give milk and has only had " + foodCount + " meals.");
		}
	}

	@Override
	public void makeSound() {
		// TODO Auto-generated method stub

	}

}
