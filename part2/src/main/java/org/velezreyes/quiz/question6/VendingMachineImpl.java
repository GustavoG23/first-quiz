package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

    private Map<String, Integer> drinkPrices;
    private Map<String, Boolean> drinkFizzy;
    private int balance;

    private static VendingMachineImpl instance;

    private VendingMachineImpl() {
        drinkPrices = new HashMap<>();
        drinkFizzy = new HashMap<>();
        balance = 0;

        // Define drink prices and fizziness
        drinkPrices.put("ScottCola", 75);
        drinkPrices.put("KarenTea", 100);
        drinkFizzy.put("ScottCola", true);
        drinkFizzy.put("KarenTea", false);
    }

    public static VendingMachine getInstance() {
        if (instance == null) {
            instance = new VendingMachineImpl();
        }
        return instance;
    }

    @Override
    public void insertQuarter() {
        balance += 25;
    }

    @Override
    public Drink pressButton(String drinkName) throws NotEnoughMoneyException, UnknownDrinkException {
        if (drinkPrices.containsKey(drinkName)) {
            int price = drinkPrices.get(drinkName);
            boolean isFizzy = drinkFizzy.get(drinkName);

            if (balance >= price) {
                balance -= price;
                return new Drink(drinkName, isFizzy);
            } else {
                throw new NotEnoughMoneyException();
            }
        } else {
            throw new UnknownDrinkException();
        }
    }
}
