import { Link } from "react-router-dom";
import type { Recipe } from "/helpers/recipes";
import { elicitRecipes, primerRecipes } from "/helpers/recipes";
import React, { useEffect } from "react";

interface RecipeGroupProps {
  title: string;
  recipes: Record<string, Recipe>; // assuming traceId is a string
  children?: React.ReactNode;
}

function RecipeGroup({ title, recipes, children }: RecipeGroupProps) {
  return (
    <>
      <h2 className="text-lg font-semibold mt-8">{title}</h2>
      <div className="p-2 pl-0">{children}</div>
      <ul className="grid grid-cols-1 list-none">
        {Object.entries(recipes).map(([traceId, { title, description, hidden }]) => {
          if (hidden) return null;
          return (
            <li key={traceId} className="p-2 pl-0">
              <Link to={`/traces/${traceId}`}>
                <a className="flex items-center">
                  <div className="flex-1">
                    <h3 className="text-l font-semibold">{title}</h3>
                    <p className="text-gray-600">{description}</p>
                  </div>
                </a>
              </Link>
            </li>
          );
        })}
      </ul>
    </>
  );
}

export default function HomePage() {
  useEffect(() => {
    document.title = "Interactive Composition Explorer (ICE)";
  }, []);
  return (
    <div className="m-12">
      <h1 className="text-xl font-bold mb-2">Heurist Trace Visualizer</h1>
      <p>
        This is a trace visualizer for the Heurist Agent Framework.
        <a href="https://github.com/heurist-network/heurist-agent-framework">Heurist Agent Framework</a>
      </p>
      <p>
        Learn more about Heurist at <a href="https://www.heurist.ai">Heurist AI</a>
      </p>
      <p>
        Based on the ICE repo <a href="https://github.com/oughtinc/ice">ICE</a> 
      </p>
      <div className="p-2 pl-0">
        <Link to="traces/">You can view your own traces here.</Link>
      </div>
    </div>
  );
}
