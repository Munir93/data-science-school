public class Player {

    private String name;
    private int exp;
    private  int level;

    public Player(String name, int exp, int level) {
        this.name = name;
        this.exp = exp;
        this.level = level;
    }

    public String getName() {
        return name;
    }

    public int getExp() {
        return exp;
    }

    public int getLevel() {
        return level;
    }

    public int increaseExp(){
        return this.exp+10;
    }

    public int increaseLevel(){
        return this.level++;
    }

    public void setExp(int exp) {
        this.exp = exp;
    }
}
