"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import HomePage from "../components/HomePage";
import { useTranslation } from "react-i18next";

export default function Home() {
  const { t } = useTranslation();
  const router = useRouter();
  const [hasStory, setHasStory] = useState(false);

  useEffect(() => {
    const storedStoryId = localStorage.getItem("storyId");
    if (storedStoryId) {
      setHasStory(true); // Indica que existe una historia guardada
    }
  }, []);

  const handleContinue = () => {
    router.push("/adventure"); // Redirige solo cuando el usuario lo decide
  };

  return (
    <main>
      <HomePage />

      {hasStory && (
        <div className="continue-container">
          <p>{t("home.continuePrompt")}</p>
          <button className="continue-button" onClick={handleContinue}>
            {t("home.continueButton")}
          </button>
        </div>
      )}
    </main>
  );
}
