package AnimalsPackage;
public abstract class Feline extends Animal{
	
	int lives;

	public Feline(double weight) {
		super(weight);
	}

	public Feline(double weight, String food) {
		super(weight);
		this.addFood(food);
	}
	
	public Feline() {
		super(0);
	}
	
	public int getLives() {
		return lives;
	}

}
