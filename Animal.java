package AnimalsPackage;
import java.util.ArrayList;

public abstract class Animal {
	public double weight;
	private ArrayList<String> foods;

	public Animal(double weight) {
		this.weight = weight;
		this.foods = new ArrayList<String>();
	}

	public void addFood(String food) {
		this.foods.add(food);
	}

	public void removeFood(String food) {
		this.foods.remove(food);
	}

	public void printFoods() {
		for (String f : foods) {
			System.out.println(f);
		}
	}
	
	public abstract void makeSound();
}