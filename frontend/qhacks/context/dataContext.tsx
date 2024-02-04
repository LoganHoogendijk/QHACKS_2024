"use client";

import { createContext, useContext, useState, useEffect } from "react";

const DataContext = createContext({});

export function useData() {
  return useContext(DataContext);
}

export function DataProvider({ children }: any) {
  const [plants, setPlants] = useState([]);
  const [selectedPlant, setSelectedPlant] = useState({});

  const value = {
    plants,
    selectedPlant,
    setPlants,
    setSelectedPlant,
  };

  return <DataContext.Provider value={value}>{children}</DataContext.Provider>;
}
