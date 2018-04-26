public class Monsters {

    private String name;
    private  int health;
    private int damage;

    public Monsters( String name, int health, int damage){
        this.damage = damage;
        this.health = health;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }

    public int getDamage() {
        return damage;
    }
}
