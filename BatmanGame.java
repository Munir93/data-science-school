
import java.util.Random;
import java.util.Scanner;

public class BatmanGame {

    public void start() {
        // Scanner for taking user input and Random for generating random numbers in the game
        Scanner myScanner = new Scanner(System.in);
        Random randomNumberGen = new Random();

        int healthPotionHealAmmount = 20;
        int chanceOfPotionDrop = 40;
        int numberOfMonstersKilled = 0;

        Boolean gameOn = true;  // condition for while loop

        Player newPlayer = new Player("Player1",10,1);







        // Here I use the Monsters class to create new monster objects

        Monsters joker = new Monsters("Joker", 100, 90);
        Monsters bain = new Monsters("Bain", 85, 100);
        Monsters penguin = new Monsters("Penguin", 50, 40);
        Monsters superman = new Monsters("SuperMan", 300, 120);
        Monsters poisonIvy = new Monsters("Poison Ivy", 65, 55);

        // Here I store the new monsters in an array
        Monsters[] monstersList = {joker, bain, penguin, superman, poisonIvy};

        // Next I am creating the Hero

        Hero batman = new Hero("BatMan", 120, 50, 4);
        Hero robin = new Hero("Robin", 75, 35, 2);

        // Heroes are also stored in an array
        Hero[] heroList = {batman, robin};

        System.out.println("Welcome to Batman adventure game!");
        System.out.println("");

        System.out.println("What is your name?");


        // Player selects hero of choice
        System.out.println("Please select your Hero: ");
        System.out.println("\t1. Batman            \n\t\t Batmans Stats  " + "\n\t\t Health: " + batman.getHealth() + "\n\t\t Attack Damage: " + batman.getAttackDamage() + "\n\t\t Starting number of Health Potions: " + batman.getNumOfHealthPotions());
        System.out.println("\t2. Robin              \n\t\t Robins Stats " + "\n\t\t Health: " + robin.getHealth() + "\n\t\t Attack Damage: " + robin.getAttackDamage() + "\n\t\t Starting number of Health Potions: " + robin.getNumOfHealthPotions());

        String input = myScanner.nextLine();
        Hero theChosenHero;
        if (input.equals("1")) {
            theChosenHero = heroList[0];
            System.out.println("You have chosen " + theChosenHero.getHeroName());
        } else if (input.equals("2")) {
            theChosenHero = heroList[1];
            System.out.println("You have chosen " + theChosenHero.getHeroName());
        } else {theChosenHero = heroList[randomNumberGen.nextInt((heroList.length))];
            System.out.println("Failed to select a valid Hero. Random hero selected");
            System.out.println("\t> " + theChosenHero.getHeroName() + " is the chosen Hero");}


        // Start of logic for game
        // While Loop label so we can tell program when to start from beginning of loop
        GAMEON:
        while (gameOn) {
            System.out.println("/./././././././././././././././././././././././././");


            //Selects random Monster from list of monsters
            Monsters monsters = monstersList[randomNumberGen.nextInt(monstersList.length)];
            // generates a random value for the monsters health using the value defined in object as a max
            int monstersHealth = randomNumberGen.nextInt(monsters.getHealth());
            System.out.println("\t# " + monsters.getName() + " has appeared! #\n");

            // while the monsters health is greater than 0 the battle will continue
            while (monstersHealth > 0) {

                System.out.println("\tYour HP: " + theChosenHero.getHealth());
                System.out.println("\t" + monsters.getName() + "'s HP: " + monstersHealth);
                System.out.println("\n\tWhat would you like to do?");
                System.out.println("\t1. Jump");
                System.out.println("\t2. Fight");
                System.out.println("\t3. Drink health potion");

                input = myScanner.next();

                if (input.equals("1")) {
                    System.out.println("You jumped over " + monsters.getName());
                    continue GAMEON;

                } else if (input.equals("2")) {
                    int damageDealt = theChosenHero.getAttackDamage();
                    if (damageDealt >= monstersHealth) {
                        monstersHealth = monstersHealth - damageDealt;
                        System.out.println("\t> You strike " + monsters.getName() + " and have killed him");
                        numberOfMonstersKilled++;
                    } else {
                        System.out.println("\t> You strike " + monsters.getName() + " and dealt " + damageDealt + "  worth of damage but were unable to kill him...");
                        System.out.println("\t> " + monsters.getName() + " attacked you back!!");
                        int damageTaken = randomNumberGen.nextInt(monsters.getDamage());
                        System.out.println("\t> You lost " + damageTaken + " health points during the battle");
                        theChosenHero.setHealth(theChosenHero.getHealth() - damageTaken);
                        monstersHealth = monstersHealth - damageDealt;
                        System.out.println("\t> Your current health is: " + theChosenHero.getHealth());
                    }
                    if (theChosenHero.getHealth() >= 10 && theChosenHero.getHealth() <= 20) {
                        System.out.println("\t> You have taken a lot of damage. Continue with caution and take a Health potion when you can");
                    }
                    if (theChosenHero.getHealth() < 10) {
                        System.out.println("\t> You are to weak to continue!!!");
                        System.out.println("/././././././././././././././././././././././././././././././././");
                        System.out.println("\t> !!!!GAME OVER!!!!");
                        break;
                    }
                } else if (input.equals("3")) {

                    if (theChosenHero.getNumOfHealthPotions() > 0) {
                        System.out.println("\t> Drinking health potion");
                        theChosenHero.setHealth(theChosenHero.getHealth() + healthPotionHealAmmount);
                        if (theChosenHero.getHealth() > 100) {
                            System.out.println("\t> You have been healed to max health");
                            theChosenHero.setHealth(100);
                        } else {
                            System.out.println("\t> Your health has risen by: " + healthPotionHealAmmount + " Your health is now: " + theChosenHero.getHealth());
                        }
                        theChosenHero.decreaseNumOfHealthPotions();
                        System.out.println("\t> You have+ " + theChosenHero.getNumOfHealthPotions() + " remaining!");
                    } else {
                        System.out.println("\t> You are all out of health potions!");
                        System.out.println("\t> Continue fighting in order to get more health potions");
                    }
                } else {
                    System.out.println("\t> Invalid command! Please Enter a valid command!");
                }
            }
            if (theChosenHero.getHealth() < 1) {
                System.out.println("\t> You are to weak to continue");
                System.out.println("/././././././././././././././././././././././././././././././././");
                System.out.println("\t> !!!!GAME OVER!!!!");
                break;
            }
            System.out.println("/././././././././././././././././././././././././././././././././././.");
            System.out.println("\t> Well done you saved the city " + monsters.getName() + " was defeated! ");
            System.out.println("\t> You have " + theChosenHero.getHealth() + "HP left ");
            // If the random number is less than 50 it drops
            if (randomNumberGen.nextInt(100) < chanceOfPotionDrop) {
                theChosenHero.increaseNumOfHealthPotions();
                System.out.println("\t> The " + monsters.getName() + " dropped a health potion. ");
                System.out.println("\t>  You now have " + theChosenHero.getNumOfHealthPotions() + " health potion(s). ");
            }
            System.out.println("/././././././././././././././././././././././././././././././././././");
            System.out.println("\t> What would you like to do now?");
            System.out.println("\t> 1. Continue exploring");
            System.out.println("\t> 2. Exit the city and return to the BatCave");
            input = myScanner.nextLine();

            while (!input.equals("1") && !input.equals("2")) {
                System.out.println("\t> Invalid command");
                input = myScanner.nextLine();
            }
            if (input.equals("1")) {
                System.out.println("\t> You arn't done yet! On to the next Monster");
            } else if (input.equals("2")) {
                System.out.println("\t> Returning to the batcave.");
                break;
            }

        }
        System.out.println("\t> Thank you for playing");
        System.out.println("\t> You managed to kill " + numberOfMonstersKilled + " Monsters");
        newPlayer.setExp(newPlayer.getExp() + numberOfMonstersKilled*10);
        System.out.println("Your exp is now " + newPlayer.getExp());
        System.out.println("\t> Do you want to play again?");
        System.out.println("\t> 1. Yes");
        System.out.println("\t> 2. No");
        input = myScanner.nextLine();

        while (!input.equals("1") && !input.equals("2")) {
            System.out.println("\t> Invalid command");
            input = myScanner.nextLine();
        }
        if (input.equals("1")) {
            System.out.println("\t> Loading your game!!!");
            replay();
        } else if (input.equals("2")) {
            System.out.println("\t> Goodbye!!!");
        }


    }
    public void replay(){
        start();
    }

}
