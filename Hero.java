public class Hero {

    private String HeroName;
    private int health;
    private int attackDamage;
    private int numOfHealthPotions;


    public Hero(String heroName, int health, int attackDamage, int numOfHealthPotions) {
        HeroName = heroName;
        this.health = health;
        this.attackDamage = attackDamage;
        this.numOfHealthPotions = numOfHealthPotions;
    }

    public String getHeroName() {
        return HeroName;
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getAttackDamage() {
        return attackDamage;
    }

    public int getNumOfHealthPotions() {
        return numOfHealthPotions;
    }

    public int increaseNumOfHealthPotions(){
        return this.numOfHealthPotions++;
    }

    public int decreaseNumOfHealthPotions(){
        return this.numOfHealthPotions--;
    }
}



