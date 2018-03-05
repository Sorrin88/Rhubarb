package AnimalsPackage;
public abstract class Canine extends Animal{
	
	int packSize;

	public Canine(double weight) {
		super(weight);
	}

	public Canine(double weight, String food) {
		super(weight);
		this.addFood(food);
	}
	
	public Canine() {
		super(0);
	}
	
	public int getPackSize() {
		return packSize;
	}

}
