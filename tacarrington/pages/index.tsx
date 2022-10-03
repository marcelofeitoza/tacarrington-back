import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import styles from "../styles/home.module.scss";
import wave from "../public/wave.svg";
import logo from "../public/logo.svg";
import { FiDownload, FiActivity, FiArrowUp, FiRadio } from "react-icons/fi";

const Home: NextPage = () => {
  const todayData = {
    title: "Solar storm event",
    time: "00:00:00.078 - 2022/01/01",
    magnitude: 8.32856,
  };

  const weekData = [
    {
      title: "Solar storm event",
      time: "2022/01/01 00:00:00.170",
      magnitude: 8.314696,
    },
    {
      title: "Solar storm event",
      time: "2022/01/01 00:00:00.262",
      magnitude: 8.315007,
    },
    {
      title: "Solar storm event",
      time: "2022/01/01 00:00:00.354",
      magnitude: 8.316628,
    },
    {
      title: "Solar storm event",
      time: "2022/01/01 00:00:00.446",
      magnitude: 8.352105,
    },
    {
      title: "Solar storm event",
      time: "2022/01/01 00:00:00.538",
      magnitude: 8.3481,
    }
  ];

  return (
    <main className={styles.main}>
      <div>
        <header>
          <Image src={logo} width="40px" alt="solar waves" />
          <h1>taCarrington</h1>
        </header>
        <div className={styles.data}>
          <FiActivity size={30} />
          <h2>{todayData.magnitude}</h2>

          <span>
            <FiArrowUp color="#00FF47" />
            <h5>1%</h5>
          </span>
          <div>
            <span>01/01/2022</span>
            <span>00 AM</span>
          </div>
        </div>
        <Image src={wave} className={styles.image} alt="solar waves" />

        <footer>
          <span>Atualizado há 15 minutos</span>
        </footer>
      </div>
      <div>
        <header>
          <button>
            <FiDownload />
          </button>
        </header>
        <div className={styles.cards}>
          <div>
            <span>Magnitude</span>
            <h1>
              {todayData.magnitude} <span>keV</span>
            </h1>
          </div>
          <div>
            <span>Time</span>
            <h1>
              {todayData.time}
            </h1>
          </div>
        </div>
        <div className={styles.events}>
          <header>
            <FiRadio size={22} />
            <h2>Next events</h2>
          </header>
          <div>
            {weekData.map((e) => (
              <div key={e.time}>
                <div>
                  <h2>{e.title}</h2>
                  <span>{e.time}</span>
                </div>
                <h1>{e.magnitude} keV</h1>
              </div>
            ))}
          </div>
        </div>
      </div>
    </main>
  );
};

export default Home;
