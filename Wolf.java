package AnimalsPackage;
public class Wolf extends Canine {

	public Wolf(double weight, String food) {
		super(weight);
		this.addFood(food);
		packSize = 15;
	}

	@Override
	public void makeSound() {
		System.out.println("AROOOOO");
	}
	
}