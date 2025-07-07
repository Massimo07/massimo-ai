import { useLang } from "../i18n";

export default function Welcome() {
  const { lang, setLang, t } = useLang();

  return (
    <div className="p-6 text-center">
      <div className="mb-4">
        <select value={lang} onChange={e => setLang(e.target.value)}>
          <option value="it">🇮🇹 Italiano</option>
          <option value="en">🇬🇧 English</option>
          <option value="es">🇪🇸 Español</option>
          <option value="fr">🇫🇷 Français</option>
          <option value="de">🇩🇪 Deutsch</option>
        </select>
      </div>
      <h1 className="text-2xl font-bold">{t("welcome")}</h1>
    </div>
  );
}
