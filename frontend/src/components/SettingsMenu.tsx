import React, { useEffect, useRef } from "react";

interface SettingsMenuProps {
  typingEffect: boolean;
  setTypingEffect: (value: boolean) => void;
  typingSpeed: number;
  setTypingSpeed: (value: number) => void;
}

export const SettingsMenu: React.FC<SettingsMenuProps> = ({
  typingEffect,
  setTypingEffect,
  typingSpeed,
  setTypingSpeed,
}) => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (ref.current && !ref.current.contains(event.target as Node)) {
        console.log("Clic fuera del menú de configuración");
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="settings-menu" ref={ref}>
      <label>
        <input
          type="checkbox"
          checked={typingEffect}
          onChange={() => setTypingEffect(!typingEffect)}
        />
        Efecto máquina de escribir
      </label>
      <br />
      <label>
        Velocidad base (ms):
        <input
          type="number"
          value={typingSpeed}
          onChange={(e) => setTypingSpeed(parseInt(e.target.value, 10))}
          disabled={!typingEffect}
        />
      </label>
    </div>
  );
};
