package AnimalsPackage;
public class Lion extends Feline {

	public Lion(double weight, String food) {
		super(weight);
		this.addFood(food);
		lives = 3;
	}

	@Override
	public void makeSound() {
		System.out.println("ROOOAAAR");
	}
	
}