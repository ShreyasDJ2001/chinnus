{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "428a4281",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import seaborn as sns \n",
    "import matplotlib.pyplot as plt \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4c619b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_data=pd.read_excel(r'C:\\Users\\Shreyas\\Downloads\\datata/Data_Train.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bf0f4eca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Date_of_Journey</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>24/03/2019</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>22:20</td>\n",
       "      <td>01:10 22 Mar</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>1/05/2019</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>05:50</td>\n",
       "      <td>13:15</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>9/06/2019</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>09:25</td>\n",
       "      <td>04:25 10 Jun</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>12/05/2019</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>18:05</td>\n",
       "      <td>23:30</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>01/03/2019</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>16:50</td>\n",
       "      <td>21:35</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10678</th>\n",
       "      <td>Air Asia</td>\n",
       "      <td>9/04/2019</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → BLR</td>\n",
       "      <td>19:55</td>\n",
       "      <td>22:25</td>\n",
       "      <td>2h 30m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>4107</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10679</th>\n",
       "      <td>Air India</td>\n",
       "      <td>27/04/2019</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → BLR</td>\n",
       "      <td>20:45</td>\n",
       "      <td>23:20</td>\n",
       "      <td>2h 35m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>4145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10680</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>27/04/2019</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>08:20</td>\n",
       "      <td>11:20</td>\n",
       "      <td>3h</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>7229</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10681</th>\n",
       "      <td>Vistara</td>\n",
       "      <td>01/03/2019</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>11:30</td>\n",
       "      <td>14:10</td>\n",
       "      <td>2h 40m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>12648</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10682</th>\n",
       "      <td>Air India</td>\n",
       "      <td>9/05/2019</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → GOI → BOM → COK</td>\n",
       "      <td>10:55</td>\n",
       "      <td>19:15</td>\n",
       "      <td>8h 20m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>11753</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10683 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           Airline Date_of_Journey    Source Destination  \\\n",
       "0           IndiGo      24/03/2019  Banglore   New Delhi   \n",
       "1        Air India       1/05/2019   Kolkata    Banglore   \n",
       "2      Jet Airways       9/06/2019     Delhi      Cochin   \n",
       "3           IndiGo      12/05/2019   Kolkata    Banglore   \n",
       "4           IndiGo      01/03/2019  Banglore   New Delhi   \n",
       "...            ...             ...       ...         ...   \n",
       "10678     Air Asia       9/04/2019   Kolkata    Banglore   \n",
       "10679    Air India      27/04/2019   Kolkata    Banglore   \n",
       "10680  Jet Airways      27/04/2019  Banglore       Delhi   \n",
       "10681      Vistara      01/03/2019  Banglore   New Delhi   \n",
       "10682    Air India       9/05/2019     Delhi      Cochin   \n",
       "\n",
       "                       Route Dep_Time  Arrival_Time Duration Total_Stops  \\\n",
       "0                  BLR → DEL    22:20  01:10 22 Mar   2h 50m    non-stop   \n",
       "1      CCU → IXR → BBI → BLR    05:50         13:15   7h 25m     2 stops   \n",
       "2      DEL → LKO → BOM → COK    09:25  04:25 10 Jun      19h     2 stops   \n",
       "3            CCU → NAG → BLR    18:05         23:30   5h 25m      1 stop   \n",
       "4            BLR → NAG → DEL    16:50         21:35   4h 45m      1 stop   \n",
       "...                      ...      ...           ...      ...         ...   \n",
       "10678              CCU → BLR    19:55         22:25   2h 30m    non-stop   \n",
       "10679              CCU → BLR    20:45         23:20   2h 35m    non-stop   \n",
       "10680              BLR → DEL    08:20         11:20       3h    non-stop   \n",
       "10681              BLR → DEL    11:30         14:10   2h 40m    non-stop   \n",
       "10682  DEL → GOI → BOM → COK    10:55         19:15   8h 20m     2 stops   \n",
       "\n",
       "      Additional_Info  Price  \n",
       "0             No info   3897  \n",
       "1             No info   7662  \n",
       "2             No info  13882  \n",
       "3             No info   6218  \n",
       "4             No info  13302  \n",
       "...               ...    ...  \n",
       "10678         No info   4107  \n",
       "10679         No info   4145  \n",
       "10680         No info   7229  \n",
       "10681         No info  12648  \n",
       "10682         No info  11753  \n",
       "\n",
       "[10683 rows x 11 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "543a9f59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Airline            0\n",
       "Date_of_Journey    0\n",
       "Source             0\n",
       "Destination        0\n",
       "Route              1\n",
       "Dep_Time           0\n",
       "Arrival_Time       0\n",
       "Duration           0\n",
       "Total_Stops        1\n",
       "Additional_Info    0\n",
       "Price              0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5fcc7887",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10683, 11)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "37aa73ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_data.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bba2f33f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Airline            0\n",
       "Date_of_Journey    0\n",
       "Source             0\n",
       "Destination        0\n",
       "Route              0\n",
       "Dep_Time           0\n",
       "Arrival_Time       0\n",
       "Duration           0\n",
       "Total_Stops        0\n",
       "Additional_Info    0\n",
       "Price              0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "30572d05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Airline            object\n",
       "Date_of_Journey    object\n",
       "Source             object\n",
       "Destination        object\n",
       "Route              object\n",
       "Dep_Time           object\n",
       "Arrival_Time       object\n",
       "Duration           object\n",
       "Total_Stops        object\n",
       "Additional_Info    object\n",
       "Price               int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.dtypes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6ff9ceca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def change_into_datetime(col):\n",
    "    \n",
    "    train_data[col]=pd.to_datetime(train_data[col])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a0be5cd7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Airline', 'Date_of_Journey', 'Source', 'Destination', 'Route',\n",
       "       'Dep_Time', 'Arrival_Time', 'Duration', 'Total_Stops',\n",
       "       'Additional_Info', 'Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "230d8959",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in ['Date_of_Journey','Dep_Time', 'Arrival_Time']:\n",
    "    change_into_datetime(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "eb17c843",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Airline                    object\n",
       "Date_of_Journey    datetime64[ns]\n",
       "Source                     object\n",
       "Destination                object\n",
       "Route                      object\n",
       "Dep_Time           datetime64[ns]\n",
       "Arrival_Time       datetime64[ns]\n",
       "Duration                   object\n",
       "Total_Stops                object\n",
       "Additional_Info            object\n",
       "Price                       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f4f73098",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Date_of_Journey</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>2019-03-24</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2022-04-24 22:20:00</td>\n",
       "      <td>2022-03-22 01:10:00</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>2019-01-05</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>2022-04-24 05:50:00</td>\n",
       "      <td>2022-04-24 13:15:00</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>2019-09-06</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>2022-04-24 09:25:00</td>\n",
       "      <td>2022-06-10 04:25:00</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>2019-12-05</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>2022-04-24 18:05:00</td>\n",
       "      <td>2022-04-24 23:30:00</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>2019-01-03</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>2022-04-24 16:50:00</td>\n",
       "      <td>2022-04-24 21:35:00</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline Date_of_Journey    Source Destination                  Route  \\\n",
       "0       IndiGo      2019-03-24  Banglore   New Delhi              BLR → DEL   \n",
       "1    Air India      2019-01-05   Kolkata    Banglore  CCU → IXR → BBI → BLR   \n",
       "2  Jet Airways      2019-09-06     Delhi      Cochin  DEL → LKO → BOM → COK   \n",
       "3       IndiGo      2019-12-05   Kolkata    Banglore        CCU → NAG → BLR   \n",
       "4       IndiGo      2019-01-03  Banglore   New Delhi        BLR → NAG → DEL   \n",
       "\n",
       "             Dep_Time        Arrival_Time Duration Total_Stops  \\\n",
       "0 2022-04-24 22:20:00 2022-03-22 01:10:00   2h 50m    non-stop   \n",
       "1 2022-04-24 05:50:00 2022-04-24 13:15:00   7h 25m     2 stops   \n",
       "2 2022-04-24 09:25:00 2022-06-10 04:25:00      19h     2 stops   \n",
       "3 2022-04-24 18:05:00 2022-04-24 23:30:00   5h 25m      1 stop   \n",
       "4 2022-04-24 16:50:00 2022-04-24 21:35:00   4h 45m      1 stop   \n",
       "\n",
       "  Additional_Info  Price  \n",
       "0         No info   3897  \n",
       "1         No info   7662  \n",
       "2         No info  13882  \n",
       "3         No info   6218  \n",
       "4         No info  13302  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1ea13ee2",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_data['Joruney_day']=train_data['Date_of_Journey'].dt.day\n",
    "train_data['Joruney_month']=train_data['Date_of_Journey'].dt.month\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b029157c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Date_of_Journey</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>2019-03-24</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2022-04-24 22:20:00</td>\n",
       "      <td>2022-03-22 01:10:00</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>2019-01-05</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>2022-04-24 05:50:00</td>\n",
       "      <td>2022-04-24 13:15:00</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>2019-09-06</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>2022-04-24 09:25:00</td>\n",
       "      <td>2022-06-10 04:25:00</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>2019-12-05</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>2022-04-24 18:05:00</td>\n",
       "      <td>2022-04-24 23:30:00</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>2019-01-03</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>2022-04-24 16:50:00</td>\n",
       "      <td>2022-04-24 21:35:00</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline Date_of_Journey    Source Destination                  Route  \\\n",
       "0       IndiGo      2019-03-24  Banglore   New Delhi              BLR → DEL   \n",
       "1    Air India      2019-01-05   Kolkata    Banglore  CCU → IXR → BBI → BLR   \n",
       "2  Jet Airways      2019-09-06     Delhi      Cochin  DEL → LKO → BOM → COK   \n",
       "3       IndiGo      2019-12-05   Kolkata    Banglore        CCU → NAG → BLR   \n",
       "4       IndiGo      2019-01-03  Banglore   New Delhi        BLR → NAG → DEL   \n",
       "\n",
       "             Dep_Time        Arrival_Time Duration Total_Stops  \\\n",
       "0 2022-04-24 22:20:00 2022-03-22 01:10:00   2h 50m    non-stop   \n",
       "1 2022-04-24 05:50:00 2022-04-24 13:15:00   7h 25m     2 stops   \n",
       "2 2022-04-24 09:25:00 2022-06-10 04:25:00      19h     2 stops   \n",
       "3 2022-04-24 18:05:00 2022-04-24 23:30:00   5h 25m      1 stop   \n",
       "4 2022-04-24 16:50:00 2022-04-24 21:35:00   4h 45m      1 stop   \n",
       "\n",
       "  Additional_Info  Price  Joruney_day  Joruney_month  \n",
       "0         No info   3897           24              3  \n",
       "1         No info   7662            5              1  \n",
       "2         No info  13882            6              9  \n",
       "3         No info   6218            5             12  \n",
       "4         No info  13302            3              1  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c32089a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_data.drop('Date_of_Journey',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d28340cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2022-04-24 22:20:00</td>\n",
       "      <td>2022-03-22 01:10:00</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>2022-04-24 05:50:00</td>\n",
       "      <td>2022-04-24 13:15:00</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>2022-04-24 09:25:00</td>\n",
       "      <td>2022-06-10 04:25:00</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>2022-04-24 18:05:00</td>\n",
       "      <td>2022-04-24 23:30:00</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>2022-04-24 16:50:00</td>\n",
       "      <td>2022-04-24 21:35:00</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination                  Route  \\\n",
       "0       IndiGo  Banglore   New Delhi              BLR → DEL   \n",
       "1    Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   \n",
       "2  Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK   \n",
       "3       IndiGo   Kolkata    Banglore        CCU → NAG → BLR   \n",
       "4       IndiGo  Banglore   New Delhi        BLR → NAG → DEL   \n",
       "\n",
       "             Dep_Time        Arrival_Time Duration Total_Stops  \\\n",
       "0 2022-04-24 22:20:00 2022-03-22 01:10:00   2h 50m    non-stop   \n",
       "1 2022-04-24 05:50:00 2022-04-24 13:15:00   7h 25m     2 stops   \n",
       "2 2022-04-24 09:25:00 2022-06-10 04:25:00      19h     2 stops   \n",
       "3 2022-04-24 18:05:00 2022-04-24 23:30:00   5h 25m      1 stop   \n",
       "4 2022-04-24 16:50:00 2022-04-24 21:35:00   4h 45m      1 stop   \n",
       "\n",
       "  Additional_Info  Price  Joruney_day  Joruney_month  \n",
       "0         No info   3897           24              3  \n",
       "1         No info   7662            5              1  \n",
       "2         No info  13882            6              9  \n",
       "3         No info   6218            5             12  \n",
       "4         No info  13302            3              1  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b8cb2e53",
   "metadata": {},
   "outputs": [],
   "source": [
    "def extract_hour(df,col):\n",
    "    df[col+'_hour']=df[col].dt.hour\n",
    "    \n",
    "def extract_minute(df,col):\n",
    "    df[col+'_minute']=df[col].dt.minute\n",
    "    \n",
    "def drop_column(df,col):\n",
    "    df.drop(col,axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c97842db",
   "metadata": {},
   "outputs": [],
   "source": [
    "extract_hour(train_data,'Dep_Time')\n",
    "extract_minute(train_data,'Dep_Time')\n",
    "drop_column(train_data,'Dep_Time')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e172650e",
   "metadata": {},
   "outputs": [],
   "source": [
    "extract_hour(train_data,'Arrival_Time')\n",
    "extract_minute(train_data,'Arrival_Time')\n",
    "drop_column(train_data,'Arrival_Time')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "680b9bd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination                  Route Duration  \\\n",
       "0       IndiGo  Banglore   New Delhi              BLR → DEL   2h 50m   \n",
       "1    Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   7h 25m   \n",
       "2  Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK      19h   \n",
       "3       IndiGo   Kolkata    Banglore        CCU → NAG → BLR   5h 25m   \n",
       "4       IndiGo  Banglore   New Delhi        BLR → NAG → DEL   4h 45m   \n",
       "\n",
       "  Total_Stops Additional_Info  Price  Joruney_day  Joruney_month  \\\n",
       "0    non-stop         No info   3897           24              3   \n",
       "1     2 stops         No info   7662            5              1   \n",
       "2     2 stops         No info  13882            6              9   \n",
       "3      1 stop         No info   6218            5             12   \n",
       "4      1 stop         No info  13302            3              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \n",
       "0             22               20                  1                   10  \n",
       "1              5               50                 13                   15  \n",
       "2              9               25                  4                   25  \n",
       "3             18                5                 23                   30  \n",
       "4             16               50                 21                   35  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9c605d27",
   "metadata": {},
   "outputs": [],
   "source": [
    "def flight_drop_time(x):\n",
    "    if(x>4) and (x<=8):\n",
    "        return \"early morning\"\n",
    "    elif (x>8) and (x<=12):\n",
    "        return \"morning\"\n",
    "    elif (x>12) and (x<=16):\n",
    "        return \"after noon\"\n",
    "    elif (x>16) and (x<=20): \n",
    "        return \"evening\"\n",
    "    elif (x>20) and (x<=24):\n",
    "        return \"night\"\n",
    "    else: \n",
    "        return \"late Night\"\n",
    "    \n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3dae7f75",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10678</th>\n",
       "      <td>Air Asia</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → BLR</td>\n",
       "      <td>2h 30m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>4107</td>\n",
       "      <td>4</td>\n",
       "      <td>9</td>\n",
       "      <td>19</td>\n",
       "      <td>55</td>\n",
       "      <td>22</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10679</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → BLR</td>\n",
       "      <td>2h 35m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>4145</td>\n",
       "      <td>27</td>\n",
       "      <td>4</td>\n",
       "      <td>20</td>\n",
       "      <td>45</td>\n",
       "      <td>23</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10680</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>3h</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>7229</td>\n",
       "      <td>27</td>\n",
       "      <td>4</td>\n",
       "      <td>8</td>\n",
       "      <td>20</td>\n",
       "      <td>11</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10681</th>\n",
       "      <td>Vistara</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 40m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>12648</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "      <td>14</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10682</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → GOI → BOM → COK</td>\n",
       "      <td>8h 20m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>11753</td>\n",
       "      <td>5</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "      <td>55</td>\n",
       "      <td>19</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10682 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           Airline    Source Destination                  Route Duration  \\\n",
       "0           IndiGo  Banglore   New Delhi              BLR → DEL   2h 50m   \n",
       "1        Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   7h 25m   \n",
       "2      Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK      19h   \n",
       "3           IndiGo   Kolkata    Banglore        CCU → NAG → BLR   5h 25m   \n",
       "4           IndiGo  Banglore   New Delhi        BLR → NAG → DEL   4h 45m   \n",
       "...            ...       ...         ...                    ...      ...   \n",
       "10678     Air Asia   Kolkata    Banglore              CCU → BLR   2h 30m   \n",
       "10679    Air India   Kolkata    Banglore              CCU → BLR   2h 35m   \n",
       "10680  Jet Airways  Banglore       Delhi              BLR → DEL       3h   \n",
       "10681      Vistara  Banglore   New Delhi              BLR → DEL   2h 40m   \n",
       "10682    Air India     Delhi      Cochin  DEL → GOI → BOM → COK   8h 20m   \n",
       "\n",
       "      Total_Stops Additional_Info  Price  Joruney_day  Joruney_month  \\\n",
       "0        non-stop         No info   3897           24              3   \n",
       "1         2 stops         No info   7662            5              1   \n",
       "2         2 stops         No info  13882            6              9   \n",
       "3          1 stop         No info   6218            5             12   \n",
       "4          1 stop         No info  13302            3              1   \n",
       "...           ...             ...    ...          ...            ...   \n",
       "10678    non-stop         No info   4107            4              9   \n",
       "10679    non-stop         No info   4145           27              4   \n",
       "10680    non-stop         No info   7229           27              4   \n",
       "10681    non-stop         No info  12648            3              1   \n",
       "10682     2 stops         No info  11753            5              9   \n",
       "\n",
       "       Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \n",
       "0                 22               20                  1                   10  \n",
       "1                  5               50                 13                   15  \n",
       "2                  9               25                  4                   25  \n",
       "3                 18                5                 23                   30  \n",
       "4                 16               50                 21                   35  \n",
       "...              ...              ...                ...                  ...  \n",
       "10678             19               55                 22                   25  \n",
       "10679             20               45                 23                   20  \n",
       "10680              8               20                 11                   20  \n",
       "10681             11               30                 14                   10  \n",
       "10682             10               55                 19                   15  \n",
       "\n",
       "[10682 rows x 14 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=train_data.copy()\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4394f723",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                night\n",
       "1        early morning\n",
       "2              morning\n",
       "3              evening\n",
       "4           after noon\n",
       "             ...      \n",
       "10678          evening\n",
       "10679          evening\n",
       "10680    early morning\n",
       "10681          morning\n",
       "10682          morning\n",
       "Name: Dep_Time_hour, Length: 10682, dtype: object"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"Dep_Time_hour\"].apply(flight_drop_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "12395b89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"Dep_Time_hour\"].apply(flight_drop_time).value_counts().plot(kind=\"bar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8be3a673",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly \n",
    "import cufflinks as cf \n",
    "from cufflinks.offline import go_offline \n",
    "from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f0f11797",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.2.0.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cf.go_offline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "153b47d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "marker": {
          "color": "rgba(255, 153, 51, 0.6)",
          "line": {
           "color": "rgba(255, 153, 51, 1.0)",
           "width": 1
          }
         },
         "name": "Dep_Time_hour",
         "orientation": "v",
         "text": "",
         "type": "bar",
         "x": [
          "early morning",
          "evening",
          "morning",
          "after noon",
          "night",
          "late Night"
         ],
         "y": [
          2880,
          2357,
          2209,
          1731,
          1040,
          465
         ]
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         }
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": ""
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": ""
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"944c2964-dae6-48c2-b3d3-09bc698ad4e3\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';                                    if (document.getElementById(\"944c2964-dae6-48c2-b3d3-09bc698ad4e3\")) {                    Plotly.newPlot(                        \"944c2964-dae6-48c2-b3d3-09bc698ad4e3\",                        [{\"marker\":{\"color\":\"rgba(255, 153, 51, 0.6)\",\"line\":{\"color\":\"rgba(255, 153, 51, 1.0)\",\"width\":1}},\"name\":\"Dep_Time_hour\",\"orientation\":\"v\",\"text\":\"\",\"type\":\"bar\",\"x\":[\"early morning\",\"evening\",\"morning\",\"after noon\",\"night\",\"late Night\"],\"y\":[2880,2357,2209,1731,1040,465]}],                        {\"legend\":{\"bgcolor\":\"#F5F6F9\",\"font\":{\"color\":\"#4D5663\"}},\"paper_bgcolor\":\"#F5F6F9\",\"plot_bgcolor\":\"#F5F6F9\",\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"font\":{\"color\":\"#4D5663\"}},\"xaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"\"},\"zerolinecolor\":\"#E1E5ED\"},\"yaxis\":{\"gridcolor\":\"#E1E5ED\",\"showgrid\":true,\"tickfont\":{\"color\":\"#4D5663\"},\"title\":{\"font\":{\"color\":\"#4D5663\"},\"text\":\"\"},\"zerolinecolor\":\"#E1E5ED\"}},                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('944c2964-dae6-48c2-b3d3-09bc698ad4e3');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"Dep_Time_hour\"].apply(flight_drop_time).value_counts().iplot(kind=\"bar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "63ab56a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>19h</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination                  Route Duration  \\\n",
       "0       IndiGo  Banglore   New Delhi              BLR → DEL   2h 50m   \n",
       "1    Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   7h 25m   \n",
       "2  Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK      19h   \n",
       "3       IndiGo   Kolkata    Banglore        CCU → NAG → BLR   5h 25m   \n",
       "4       IndiGo  Banglore   New Delhi        BLR → NAG → DEL   4h 45m   \n",
       "\n",
       "  Total_Stops Additional_Info  Price  Joruney_day  Joruney_month  \\\n",
       "0    non-stop         No info   3897           24              3   \n",
       "1     2 stops         No info   7662            5              1   \n",
       "2     2 stops         No info  13882            6              9   \n",
       "3      1 stop         No info   6218            5             12   \n",
       "4      1 stop         No info  13302            3              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \n",
       "0             22               20                  1                   10  \n",
       "1              5               50                 13                   15  \n",
       "2              9               25                  4                   25  \n",
       "3             18                5                 23                   30  \n",
       "4             16               50                 21                   35  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "85f81beb",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Duration' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-ab6af95a2882>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mDuration\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mDuration\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'  '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m         \u001b[1;32mpass\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;34m'h'\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mDuration\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Duration' is not defined"
     ]
    }
   ],
   "source": [
    "for i in range(len(Duration)):\n",
    "    if len(Duration[i].split('  '))==2:\n",
    "        pass\n",
    "    else:\n",
    "        if 'h' in Duration[i]:\n",
    "            Duration[i]=Duration[i] +' 0m'\n",
    "            ##durtion[i]+' '+'0m'\n",
    "        else:\n",
    "            Duration[i]='0h ' + Duration[i]\n",
    "            ##durtion[i]='0h'+' '+duration[i]\n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5aef6d78",
   "metadata": {},
   "outputs": [],
   "source": [
    "def progress_duration(x):\n",
    "    if 'h' not in x:\n",
    "        x=\"0h\"+ x\n",
    "    elif 'm' not in x:\n",
    "        x=x+\" 0m\"\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "7bdc699a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Duration']=data['Duration'].apply(progress_duration)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "e1e4f2ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination                  Route Duration  \\\n",
       "0       IndiGo  Banglore   New Delhi              BLR → DEL   2h 50m   \n",
       "1    Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   7h 25m   \n",
       "2  Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK   19h 0m   \n",
       "3       IndiGo   Kolkata    Banglore        CCU → NAG → BLR   5h 25m   \n",
       "4       IndiGo  Banglore   New Delhi        BLR → NAG → DEL   4h 45m   \n",
       "\n",
       "  Total_Stops Additional_Info  Price  Joruney_day  Joruney_month  \\\n",
       "0    non-stop         No info   3897           24              3   \n",
       "1     2 stops         No info   7662            5              1   \n",
       "2     2 stops         No info  13882            6              9   \n",
       "3      1 stop         No info   6218            5             12   \n",
       "4      1 stop         No info  13302            3              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \n",
       "0             22               20                  1                   10  \n",
       "1              5               50                 13                   15  \n",
       "2              9               25                  4                   25  \n",
       "3             18                5                 23                   30  \n",
       "4             16               50                 21                   35  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "592ce8ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2h'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"Duration\"][0].split(' ')[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "bbb0f65b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(data['Duration'][0].split(' ')[0][0:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "48f4754e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(data['Duration'][0].split(' ')[1][0:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "64e74cce",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '0h5'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-37-237d675f7250>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Duration'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36mapply\u001b[1;34m(self, func, convert_dtype, args, **kwds)\u001b[0m\n\u001b[0;32m   4136\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4137\u001b[0m                 \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mastype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobject\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_values\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 4138\u001b[1;33m                 \u001b[0mmapped\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmap_infer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconvert\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mconvert_dtype\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   4139\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4140\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmapped\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmapped\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mSeries\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\lib.pyx\u001b[0m in \u001b[0;36mpandas._libs.lib.map_infer\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m<ipython-input-37-237d675f7250>\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(x)\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Duration'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: '0h5'"
     ]
    }
   ],
   "source": [
    "data['Duration'].apply(lambda x:int(x.split(' ')[0][0:-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "dbee1f32",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-38-6bc5cc516f03>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Duration'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36mapply\u001b[1;34m(self, func, convert_dtype, args, **kwds)\u001b[0m\n\u001b[0;32m   4136\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4137\u001b[0m                 \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mastype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobject\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_values\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 4138\u001b[1;33m                 \u001b[0mmapped\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmap_infer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconvert\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mconvert_dtype\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   4139\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4140\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmapped\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmapped\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mSeries\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\lib.pyx\u001b[0m in \u001b[0;36mpandas._libs.lib.map_infer\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m<ipython-input-38-6bc5cc516f03>\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(x)\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Duration'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "data['Duration'].apply(lambda x:int(x.split(' ')[1][0:-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f5f95988",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Duration_total_min']=data[\"Duration\"].str.replace('h','*60').str.replace(' ','+').str.replace('m','*1').apply(eval)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4f60f5f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2*60+50*1'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'2*60+50*1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "3b2e42a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "170"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "eval('2*60+50*1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "684f3f7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>Duration_total_min</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>445</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>1140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>325</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>285</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination                  Route Duration  \\\n",
       "0       IndiGo  Banglore   New Delhi              BLR → DEL   2h 50m   \n",
       "1    Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   7h 25m   \n",
       "2  Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK   19h 0m   \n",
       "3       IndiGo   Kolkata    Banglore        CCU → NAG → BLR   5h 25m   \n",
       "4       IndiGo  Banglore   New Delhi        BLR → NAG → DEL   4h 45m   \n",
       "\n",
       "  Total_Stops Additional_Info  Price  Joruney_day  Joruney_month  \\\n",
       "0    non-stop         No info   3897           24              3   \n",
       "1     2 stops         No info   7662            5              1   \n",
       "2     2 stops         No info  13882            6              9   \n",
       "3      1 stop         No info   6218            5             12   \n",
       "4      1 stop         No info  13302            3              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \\\n",
       "0             22               20                  1                   10   \n",
       "1              5               50                 13                   15   \n",
       "2              9               25                  4                   25   \n",
       "3             18                5                 23                   30   \n",
       "4             16               50                 21                   35   \n",
       "\n",
       "   Duration_total_min  \n",
       "0                 170  \n",
       "1                 445  \n",
       "2                1140  \n",
       "3                 325  \n",
       "4                 285  "
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "f1355ba5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x277f3334cd0>"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(x='Duration_total_min',y='Price',data=data)\n",
    "# data analysis of duration_time _min vs price "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "017c36e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Destination'].unique()\n",
    "#maximum number of fligghts the destination\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "c77f5ae9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Destination'>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data['Destination'].value_counts().plot(kind='pie')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "1b3ebc7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                    BLR → DEL\n",
       "1        CCU → IXR → BBI → BLR\n",
       "2        DEL → LKO → BOM → COK\n",
       "3              CCU → NAG → BLR\n",
       "4              BLR → NAG → DEL\n",
       "                 ...          \n",
       "10678                CCU → BLR\n",
       "10679                CCU → BLR\n",
       "10680                BLR → DEL\n",
       "10681                BLR → DEL\n",
       "10682    DEL → GOI → BOM → COK\n",
       "Name: Route, Length: 10682, dtype: object"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Route']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "9f5c91ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2         True\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "10678    False\n",
       "10679    False\n",
       "10680     True\n",
       "10681    False\n",
       "10682    False\n",
       "Name: Airline, Length: 10682, dtype: bool"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Airline']=='Jet Airways'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "d31c5e68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Route\n",
       "CCU → BOM → BLR          930\n",
       "DEL → BOM → COK          875\n",
       "BLR → BOM → DEL          385\n",
       "BLR → DEL                382\n",
       "CCU → DEL → BLR          300\n",
       "BOM → HYD                207\n",
       "DEL → JAI → BOM → COK    207\n",
       "DEL → AMD → BOM → COK    141\n",
       "DEL → IDR → BOM → COK     86\n",
       "DEL → NAG → BOM → COK     61\n",
       "DEL → ATQ → BOM → COK     38\n",
       "DEL → COK                 34\n",
       "DEL → BHO → BOM → COK     29\n",
       "DEL → BDQ → BOM → COK     28\n",
       "DEL → LKO → BOM → COK     25\n",
       "DEL → JDH → BOM → COK     23\n",
       "CCU → GAU → BLR           22\n",
       "DEL → MAA → BOM → COK     16\n",
       "DEL → IXC → BOM → COK     13\n",
       "BLR → MAA → DEL           10\n",
       "BLR → BDQ → DEL            8\n",
       "DEL → UDR → BOM → COK      7\n",
       "BOM → DEL → HYD            5\n",
       "CCU → BOM → PNQ → BLR      4\n",
       "BLR → BOM → JDH → DEL      3\n",
       "DEL → DED → BOM → COK      2\n",
       "BOM → BDQ → DEL → HYD      2\n",
       "DEL → CCU → BOM → COK      1\n",
       "BOM → VNS → DEL → HYD      1\n",
       "BOM → UDR → DEL → HYD      1\n",
       "BOM → JDH → DEL → HYD      1\n",
       "BOM → IDR → DEL → HYD      1\n",
       "BOM → DED → DEL → HYD      1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['Airline']=='Jet Airways'].groupby('Route').size().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "6daa4beb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]),\n",
       " [Text(0, 0, 'IndiGo'),\n",
       "  Text(1, 0, 'Air India'),\n",
       "  Text(2, 0, 'Jet Airways'),\n",
       "  Text(3, 0, 'SpiceJet'),\n",
       "  Text(4, 0, 'Multiple carriers'),\n",
       "  Text(5, 0, 'GoAir'),\n",
       "  Text(6, 0, 'Vistara'),\n",
       "  Text(7, 0, 'Air Asia'),\n",
       "  Text(8, 0, 'Vistara Premium economy'),\n",
       "  Text(9, 0, 'Jet Airways Business'),\n",
       "  Text(10, 0, 'Multiple carriers Premium economy'),\n",
       "  Text(11, 0, 'Trujet')])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "sns.boxplot(x='Airline',y='Price',data=data)\n",
    "plt.xticks(rotation='vertical')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "034e0504",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]),\n",
       " [Text(0, 0, 'IndiGo'),\n",
       "  Text(1, 0, 'Air India'),\n",
       "  Text(2, 0, 'Jet Airways'),\n",
       "  Text(3, 0, 'SpiceJet'),\n",
       "  Text(4, 0, 'Multiple carriers'),\n",
       "  Text(5, 0, 'GoAir'),\n",
       "  Text(6, 0, 'Vistara'),\n",
       "  Text(7, 0, 'Air Asia'),\n",
       "  Text(8, 0, 'Vistara Premium economy'),\n",
       "  Text(9, 0, 'Jet Airways Business'),\n",
       "  Text(10, 0, 'Multiple carriers Premium economy'),\n",
       "  Text(11, 0, 'Trujet')])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA44AAAHmCAYAAAA8z9CKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAB90UlEQVR4nOzdd5hU9dnG8e8z2+kd6U0sgKAUxRpFRSyxxRZjYqzpGt8Y02NiitEYW4pJLARNjL3FAiigiEpTaYoISu8sfdm+z/vHObPswrIssLtnyv25rrlm5jcz6z3jMDPP+TVzd0RERERERET2JBZ1ABEREREREUlsKhxFRERERESkViocRUREREREpFYqHEVERERERKRWKhxFRERERESkViocRUREREREpFYNVjia2SNmts7M5lVpa2Nmr5vZwvC8dZXbfmJmi8xsgZmdUaV9iJnNDW+738wsbM8xsyfD9mlm1rPKY64M/xsLzezKhnqOIiIiIiIi6aAhexz/BYzape3HwAR37wtMCK9jZv2Ay4D+4WP+ZmYZ4WMeAK4H+oan+N+8Btjk7gcD9wB3hH+rDXArcAxwNHBr1QJVRERERERE9k1mQ/1hd59ctRcwdB5wcnh5DPAm8KOw/Ql3LwYWm9ki4GgzWwK0cPf3AMzsUeB84LXwMb8K/9YzwF/C3sgzgNfdfWP4mNcJis3/1pa3Xbt23rPnrnFFRERERETSw/vvv7/B3dvXdFuDFY570NHdVwO4+2oz6xC2dwGmVrnfirCtNLy8a3v8McvDv1VmZluAtlXba3hMNWZ2PUFvJt27d2fmzJn7/8xERERERESSmJkt3dNtibI4jtXQ5rW07+9jqje6/9Pdh7r70PbtayysRURERERE0l5jF45rzawTQHi+LmxfAXSrcr+uwKqwvWsN7dUeY2aZQEtgYy1/S0RERERERPZDYxeOLwHxVU6vBF6s0n5ZuFJqL4JFcKaHw1q3mdnwcP7i13Z5TPxvXQRMdHcHxgEjzax1uCjOyLBNRERERERE9kODzXE0s/8SLITTzsxWEKx0+gfgKTO7BlgGXAzg7h+Z2VPAx0AZ8B13Lw//1LcIVmjNI1gU57Ww/WHgsXAhnY0Eq7Li7hvN7DfAjPB+t8UXyhEREREREZF9Z0EnnQwdOtS1OI6IiIiIiKQrM3vf3YfWdFuiLI4jIiIiIiIiCUqFo4iIiIiIiNRKhaOIiIiIiIjUSoWjiIiIiIiI1EqFo4iIiIhIPdu6dWvUEUTqlQpHEREREZF6tGDBAi6++GLGjh0bdRSReqPCUURERESkHq1cuRKADz/8MOIkIvVHhaOIiIiIiIjUSoWjiIiIiIiI1EqFo4iIiIiIiNRKhaOIiIiIiIjUSoWjiIiIiIiI1EqFo4iIiIiIiNRKhaOIiIiIiIjUSoWjiIiIiIiI1EqFo4iIiIiIiNRKhaOIiIiISD1ydwDMLOIkIvVHhaOIiIiISD2qqKgAdhaQIqlAhaOIiIiISD2KF47qcZRUosJRRERERKQelZeXA+pxlNSiwlFEREREpB7FC0f1OEoqUeEoIiIiIlKPNMdRUpEKRxERERGRehTvcRRJJSocRURERETqkYaqSipS4SgiIiIiUo80VFVSkQpHEREREZF6pB5HSUUqHEVERERE6pG245BUpMJRRERERKQexQtHLZIjqUSFo4iIiIhIPYoXjPG5jiKpQIWjiIiIiEg9Uo+jpCIVjiIiIiIi9Ug9jpKKVDiKiIiIiNSjeOFYVlYWcRKR+qPCUURERESkHqnHUVKRCkcRERERkXoULxjV4yipRIWjiIiIiEg90uI4kopUOIqIiIiI1KOdhaOGqkrqUOEoIiIiIlKP1OMoqUiFo4iIiIhIPYrPcdTiOJJKVDiKiIiIiNQj9ThKKlLhKCIiIiJSj+I9jSocJZWocBQRERERqUfax1FSkQpHEREREZF6pDmOkopUOIqIiIiI1KPKHkcNVZUUEknhaGY3mdlHZjbPzP5rZrlm1sbMXjezheF56yr3/4mZLTKzBWZ2RpX2IWY2N7ztfjOzsD3HzJ4M26eZWc8InqaIiIiIpCF3B6BcPY6SQhq9cDSzLsANwFB3HwBkAJcBPwYmuHtfYEJ4HTPrF97eHxgF/M3MMsI/9wBwPdA3PI0K268BNrn7wcA9wB2N8NRERERERDREVVJSVENVM4E8M8sEmgCrgPOAMeHtY4Dzw8vnAU+4e7G7LwYWAUebWSeghbu/58FhnUd3eUz8bz0DnBrvjRQRERERaUiVcxw1VFVSSKMXju6+ErgLWAasBra4+3igo7uvDu+zGugQPqQLsLzKn1gRtnUJL+/aXu0x7l4GbAHa7prFzK43s5lmNnP9+vX18wRFREREJK3Fh6qq51FSSRRDVVsT9Aj2AjoDTc3sitoeUkOb19Je22OqN7j/092HuvvQ9u3b1x5cRERERKQO4gXjbj8+RZJYFENVTwMWu/t6dy8FngOOA9aGw08Jz9eF918BdKvy+K4EQ1tXhJd3ba/2mHA4bEtgY4M8GxERERGRKnZux6GhqpI6oigclwHDzaxJOO/wVGA+8BJwZXifK4EXw8svAZeFK6X2IlgEZ3o4nHWbmQ0P/87XdnlM/G9dBEz0+JgBEREREZEGFP/ZqV+fkkoyG/s/6O7TzOwZ4AOgDPgQ+CfQDHjKzK4hKC4vDu//kZk9BXwc3v877h4/fPMt4F9AHvBaeAJ4GHjMzBYR9DRe1ghPTURERESEigrNcZTU0+iFI4C73wrcuktzMUHvY033/x3wuxraZwIDamgvIiw8RUREREQak3tFtXORVBDVdhwiIiIiIikp3uOooaqSSlQ4ioiIiIjUp8o5jupxlNShwlFEREREpB5VVBaO6nKU1KHCUURERESkHnnldhzqcZTUocJRRERERKQeVWg7DklBKhxFREREROqRa46jpCAVjiIiIiIi9ajq3EbNc5RUocJRRERERKQeVZ3bqHmOkipUOIqIiIiI1KOqvYwqHCVVqHAUEREREalHXqVY1FBVSRUqHEVERERE6lG5hqpKClLhKCIiIiJSjzTHUVKRCkcRERERkXpUoaGqkoJUOIqIiIiI1KOK8vLKy+VVLoskMxWOIiIiIiL1qLyiglgsA9BQVUkdKhxFREREROpRRUU5GbEsQD2OkjpUOIqIiIiI1KPy8nIyM7MBKCsriziNSP1Q4SgiIiIiUo/Ky8vJzFCPo6QWFY4iIiIiIvWkvLwcdyczMwdQj6OkDhWOIiIiIiL1JN7DmBUWjupxlFShwlFEREREpJ7EexizsoLCsbS0NMo4IvVGhaOIiIiISD2JF4rZWbnVroskOxWOIiIiIiL1JF4oZmXmVbsukuxUOIqIiIiI1JPKHsdsFY6SWlQ4ioiIiIjUk3ihmJPdpNp1kWSnwlFEREREpJ6UlJQAOwvH+HWRZKfCUURERESknuwsHJsC6nGU1KHCUURERESknqjHUVKVCkcRERERkXpSXFwMQG5Os2rXRZKdCkcRERERkXoS72HMy1XhKKlFhaOIiIiISD0pKioCgqGqhqlwlJShwlFEREREpJ7EC8WszBwys7JVOErKUOEoIiIiIlJP4oViRkY2WZk5lT2QIslOhaOIiIiISD2p7HHMyiEzM1urqkrKUOEoIiIiIlJPioqKiMUyyIhlqsdRUooKRxERERGRelJUVER2Vi4AmZk5FBYWRpxIpH6ocBQRERERqSdFRUVkZeYAkJWRo8VxJGWocBQRERERqSdFRUVkZmYDwTzHwkINVZXUoMJRRERERKSeFBUVUVRcwJtTHyNTcxwlhahwFBERERGpJ0VFRZSXl7F+41KyMnNVOErKUOEoIiIiIlJPCguLMAt+YmtVVUklmVEHEBERERFJFatXr6KktJD1+UvZsm0dO3YURB1JpF6ocBQRERERqSdFRUW4V1BSuoOS0h0AlJWVkZmpn92S3CIZqmpmrczsGTP7xMzmm9mxZtbGzF43s4Xheesq9/+JmS0yswVmdkaV9iFmNje87X4zs7A9x8yeDNunmVnPCJ6miIiIiKSZioqK3dq0JYekgqjmON4HjHX3w4BBwHzgx8AEd+8LTAivY2b9gMuA/sAo4G9mlhH+nQeA64G+4WlU2H4NsMndDwbuAe5ojCclIiIiIumtpsJR8xwlFTR64WhmLYCTgIcB3L3E3TcD5wFjwruNAc4PL58HPOHuxe6+GFgEHG1mnYAW7v6euzvw6C6Pif+tZ4BT472RIiIiIiINwd0JfpZWpx5HSQVR9Dj2BtYDo83sQzN7yMyaAh3dfTVAeN4hvH8XYHmVx68I27qEl3dtr/YYdy8DtgBtdw1iZteb2Uwzm7l+/fr6en4iIiIikoZKS0trbFfhKKkgisIxExgMPODuRwEFhMNS96CmnkKvpb22x1RvcP+nuw9196Ht27evPbWIiIiISC32VCCqcJRUEEXhuAJY4e7TwuvPEBSSa8Php4Tn66rcv1uVx3cFVoXtXWtor/YYM8sEWgIb6/2ZiIiIiIiESkpKamxX4SipoNELR3dfAyw3s0PDplOBj4GXgCvDtiuBF8PLLwGXhSul9iJYBGd6OJx1m5kND+cvfm2Xx8T/1kXARK9pwLmIiIiISD3ZU+G4p3aRZBLVhjLfA/5jZtnA58BVBEXsU2Z2DbAMuBjA3T8ys6cIissy4DvuXh7+nW8B/wLygNfCEwQL7zxmZosIehova4wnJSIiIiLpa08F4p7mPookk0gKR3efBQyt4aZT93D/3wG/q6F9JjCghvYiwsJTRERERKQxqMdRUllU+ziKiIiIiKQUFY6SylQ4ioiIiIjUg7Kysn1qF0kmKhxFktj27duZOnVq1DFERESEPReImuMoqUCFo0gSe/DBB7n11lvZsGFD1FFERETS3p4Kx/Ly8hrbRZKJCkeRJDZ37lwACgsLI04iIiIieyoQNVRVUoEKR5EkFt+eNNjKVERERKK0p8KxoqKikZOI1D8VjiIiIiIi9SBeOObm5nL++eeTm5sLqHCU1KDCUURERESkHsRHAo0aNYpvfetbjBo1ClDhKKkhM+oAIiIiIiKpIF44jh07ttp5vF0kmalwFEli8bmN+kISERFJHEVFRbzwwguV1/U9LalAQ1VFkpgWxxEREUl8+p6WVKDCUURERERERGqlwlEkiWmoqoiISOKIxWr+aa0eR0kFKhxFUoC+kERERKK3p+/jPRWUIslE72IRERERkXqQkZFRY7sKR0kFeheLiIiIiNSDPRWOe2oXSSZ1KhzN7BAzm2Bm88LrA83s5w0bTUREREQkeWRmBjvdZWXmkJ3VhE4dDgFUOEpqqGuP44PAT4BSAHefA1zWUKFERERERJJNvHBs1eIg2rftwTmnfh+ArKysCFOJ1I+6Fo5N3H36Lm1l9R1GRERERCRZxQvH+Grn5eWlgApHSQ11LRw3mFkfwAHM7CJgdYOlEhERERFJMvEC0akAoLy8rFq7SDLLrOP9vgP8EzjMzFYCi4ErGiyViIiIiEiSyc7OBqr0OFaUVmsXSWZ1Khzd/XPgNDNrCsTcfVvDxhIRERERSS67Fo5lZSWAehwlNdR1VdXfm1krdy9w921m1trMftvQ4UREREREksXOwjEYqlpWHhSOubm5kWUSqS91neN4prtvjl9x903AWQ2SSEREREQkCcULxF17HDVUVVJBXQvHDDPLiV8xszwgp5b7i4iIiIiklZyc4OdxZY9jWDjG20WSWV0Xx/k3MMHMRhOsrHo1MKbBUomIiIiIJJns7GzMrLLHsbSsCNBQVUkNdV0c504zmwucChjwG3cf16DJRERERESSiJmRk5OLezkApWXFgApHSQ117XHE3V8DXmvALCIiIiIiSS03J4eSkrDHsTQoHPPy8qKMJFIvap3jaGZTwvNtZra1ymmbmW1tnIgiIiIiIskhNy+vco5jSWkwVFVzHCUV1Nrj6O4nhOfNGyeOiIiIiEjyatIkjx3by2jfpgelpYXk5OSSkZERdSyRA7bXVVXNLGZm8xojjIiIiIhIMmvSpAktmrXj5OFfpaSsmDzNb5QUsdfC0YO+9tlm1r0R8oiIiIiIJK28vLzK1VRLSwvJa9Ik4kQi9aOui+N0Aj4ys+lAQbzR3c9tkFQiIiIiIkmoSZMmlISFY0lpEU1UOEqKqGvh+OsGTSEiIiIikgLy8vIoKSkEoKS0kDattKKqpIZaC0czywW+CRwMzAUedveyxggmIiIiIpJsmjRpQklpUDiWlhbRtGmraAOJ1JO9zXEcAwwlKBrPBP7U4IlERERERJJUkyZNKC0tpqKigpLSQu3hKCljb0NV+7n7EQBm9jAwveEjiYiIiIgkp/icxpLSQkpLi1Q4SsrYW49jafyChqiKiIiIiNQuXjiWlhZRXLqDpk2bRpxIpH7srcdxkJltDS8bkBdeN8DdvUWDphMRERERSSLxHsai4u2UlZWqx1FSRq2Fo7tnNFYQEREREZFkF+9x3L5jU7XrIslub0NVRURERESkjuI9jAWFmwEVjpI6VDiKiIiIiNSTyh7Hgo0AGqoqKSOywtHMMszsQzN7ObzexsxeN7OF4XnrKvf9iZktMrMFZnZGlfYhZjY3vO1+M7OwPcfMngzbp5lZz0Z/giIiIiKSduKFY0E4VFWFo6SKKHscbwTmV7n+Y2CCu/cFJoTXMbN+wGVAf2AU8Dczi8+9fAC4HugbnkaF7dcAm9z9YOAe4I6GfSoiIiIiIrsPVVXhKKkiksLRzLoCZwMPVWk+DxgTXh4DnF+l/Ql3L3b3xcAi4Ggz6wS0cPf33N2BR3d5TPxvPQOcGu+NFBERERFpKLm5uQDsKNwCqHCU1BFVj+O9wC1ARZW2ju6+GiA87xC2dwGWV7nfirCtS3h51/Zqjwn3n9wCtN01hJldb2YzzWzm+vXrD/ApiYiIiEi6y8nJwSxGwY7NgApHSR2NXjia2TnAOnd/v64PqaHNa2mv7THVG9z/6e5D3X1o+/bt6xhHRERERKRmZkZubg47ioKt0FU4SqqodR/HBnI8cK6ZnQXkAi3M7N/AWjPr5O6rw2Go68L7rwC6VXl8V2BV2N61hvaqj1lhZplAS2BjQz0hEREREZG43Nw8Cgs3hpdzI04jUj8avcfR3X/i7l3dvSfBojcT3f0K4CXgyvBuVwIvhpdfAi4LV0rtRbAIzvRwOOs2Mxsezl/82i6Pif+ti8L/xm49jiIi6eShhx5ixowZUccQEUl5VYvFnJycCJOI1J8oehz35A/AU2Z2DbAMuBjA3T8ys6eAj4Ey4DvuXh4+5lvAv4A84LXwBPAw8JiZLSLoabyssZ6EiEiievrpp3n66acZN25c1FFERFJavHDMyckhFtO26ZIaIi0c3f1N4M3wcj5w6h7u9zvgdzW0zwQG1NBeRFh4iqQydaSLiIgkntzcoJcxO1u9jZI6dAhERERERKQexYenapiqpBIVjiIiIiIi9aiycMzOjjiJSP1R4SiSxIJ1oTRkVUREJJFkhwVjTq56HCV1qHAUEREREalH8R7HbPU4SgpR4SiSAuI9jyIiIhK9eMGowlFSiQpHkRSgoaoiIiKJQ4WjpCIVjiIiIiIi9SgrK6vauUgqUOEoksTiPY0aqioiIpI44gWjehwllahwFBERERGpR/HCUQd2JZWocBRJYtqOQ0REJPFoiKqkIhWOkhTKysp49NFH2bJlS9RREpKOaIqIiCSOzMxMQN/PklpUOEpSmD59Ov/5z3948skno46SUNTTKCIiknjihaO+pyWVqHCUpFBUVARAfn5+xEkSi4aqioiIJJ6MjAxAPY6SWlQ4iiQxFYwiIiKJRz2OkopUOIokMW3HISIiknjU4yipSIWjSBLTF5KIiEji0VQSSUUqHEWSmL6YRERERKQxqHAUSQHqeRQRERGRhqTCUSQFqMdRRERERBqSCkeRJKaCUUREJHFpRJCkEhWOIkks/oWkLyYREZHE0bt3b1q0aMHJJ58cdRSRepMZdQAR2X/qcRQREUk8PXv25Omnn446hki9Uo+jiIiIiIiI1EqFo4iIiIiIiNRKhaNICigtLY06goiIiIikMBWOIilgx44dUUcQERERkRSmwlEkicUXx1HhKCIiIiINSYWjSBKLb8NRVFQUcRIRERERSWUqHEWSWLxwLC8vjziJiIiIiKQyFY4iSSw+VDUW0z9lEREREWk4+rUpksTiPY7Z2dkRJxERERGRVKbCUSSJxXsc8/LyIk4iIiIiIqlMhaNIElPhKCIiIiKNQYWjSBLTUFWRA+PuLFiwQAtMiYiI7IUKR5EkFi8cMzIyIk6SWEpLS7VFyS7ivdNS3ccff8wNN9zAyy+/HHUUERGRhKbCUSSJxYuBeAEpgd///vd897vfjTpGQikrK4s6QkJau3YtEBSQIiIismeZUQcQEalv7777btQREo56HGVflZeXazSDiIhUUo9jAlq6dCnbtm2LOoYkEc3Pkr1R4Sj7Yty4cVxwwQUUFBREHUVERBKECscEdP311/PHP/4x6hiSREpKSqKOICIp5KmnnqK4uJiNGzdGHUVERBKECscENW3atKgjSBJR4Sh7o3mwsi8qKioAjWYQEZGdVDiKpIDS0tKoI0iCe/DBB6OOIElIqxOLiEicCkeRJLZlyxZAK2bK3n3++edRR5AkEu+hVuEoIiJxKhxFkli8p1ELn4hIQ4gPWRUREWn0wtHMupnZJDObb2YfmdmNYXsbM3vdzBaG562rPOYnZrbIzBaY2RlV2oeY2dzwtvstPERqZjlm9mTYPs3Mejb28xRpTPpxJyINISsrK+oIIiKSIKLocSwDfuDuhwPDge+YWT/gx8AEd+8LTAivE952GdAfGAX8zcziG0s9AFwP9A1Po8L2a4BN7n4wcA9wR2M8MZGoaAEL2RstjiP7Ij6KIS8vL+IkIiKSKBq9cHT31e7+QXh5GzAf6AKcB4wJ7zYGOD+8fB7whLsXu/tiYBFwtJl1Alq4+3sefMM9ustj4n/rGeBU068mSWFaVVX2RsOZZX/k5OREHUFERBJEpHMcwyGkRwHTgI7uvhqC4hLoEN6tC7C8ysNWhG1dwsu7tld7jLuXAVuAtjX89683s5lmNnP9+vX19KykIbzxxhtRR0hoO3bsiDqCJDgNZ66ZCuqa6ViriIjsKrLC0cyaAc8C33f3rbXdtYY2r6W9tsdUb3D/p7sPdfeh7du331tkidC6deuijpDQtm/fHnUESXDasqVm6q0XERGpm0gKRzPLIiga/+Puz4XNa8Php4Tn8UphBdCtysO7AqvC9q41tFd7jJllAi2BjfX/TESi5WEvUkFBQcRJJNEVFxdXXtac2J1UOIqIiNRNFKuqGvAwMN/d765y00vAleHlK4EXq7RfFq6U2otgEZzp4XDWbWY2PPybX9vlMfG/dREw0TUeKanpf1/NysPCUT2OsjdV9+NbvXp1hEkkGegzV0REdpUZwX/zeOCrwFwzmxW2/RT4A/CUmV0DLAMuBnD3j8zsKeBjghVZv+Pu8cPl3wL+BeQBr4UnCArTx8xsEUFP42UN/JykgWl+1u5KSkoqX5ctW7ZEnEYSXdXCcfHixXTt2rWWe6cPbTchIiJSN41eOLr7FGqegwhw6h4e8zvgdzW0zwQG1NBeRFh4SmpQ4bi75ct3rhm1ZMniCJNIMigsKsRywEuCwvHEE0+MOlJC0KqhtdNnr4iIxEW6qqpIXZWVlQFQWFgYcZLEMXfuXACa5MCKFSvZvHlztIEkYe3YsYPSklJiWZDdKsZnn30WdaSEodVDaxZ/XVQ4iohInApHSQrxFSHXr9fqqnFvv/02mRnQrEkwH+ndd9+NOpIkqE8++QQAy4aMdhV8PP9jzWGTOlHhKCIicSocJSkUh/OzVq1cqRUhgRUrVjBv3jya5EB2JrRtGeO1115VMSA1ih9UsGzI6QZbt2zl448/jjiVJLL4Z4k+U6QutmzZohFBUiePP/44d9xxB7NmzYo6iuwHFY6S8AoKCigqLiYzBkXFJSxerPl8Y8aMITPTaJoXXD+yj/PppwuZOnVqtMEk4WzdupXxr48nlgdmkNsTYtnGs889G3U0SQIqHGVvxo8fzyWXXMKll17K1q21bcst6e7DDz9kzJgxTJw4kbv/dHe1RdskOahwTDDqTdtdvBjq0MQwSPshma+//jqTJ09m6CGQEf4LHtDbaNsyxv3338fatWujDSgJ5ZFHHqGkuJiMZsH1WLbR5AjnnSnvMHv27GjDScLTHFDZmw8//BAI9oqdP39+xGkkUa1du5Y777iTDk078r2hP2DdunXcfffd+t2bZFQ4JpiVK1dGHSHhjB37GpkxaJZtHN4uk/HjxqbtB83kyZO5++676d7ROPrwnT/oMmLGWcfAju1b+NGPbmHdOs0FlWABpddee40mR4BVWUO72ZGQ1SLGPffeQ3FxcWT5JHHFC0YVjlIbd+eDD2fRtMdALCNTww+lRmvWrOGWH95C4fYivnnU9xjQfiAXHHoxb731lorHJKPCMcG89957lZfVcwSff/45c+bMpVWOAcYXemSyfkN+WvY6/u9//+P3v/8dndo45x5nZGZU/0HXvpVx/gmwMX8t3//+jSxZsiSaoJIQSktLuefee8hqEaP5sOq3xbKMFidVsHrVap544oloAookoWXLlml+cBWffPIJmzdtpHmfYTTpfChT3nlXw5ulmnXr1nHzD25m68atfH/oD+nSvBsAZ/Q+m3P7Xsgbb7zBXXfdpYW4koQKxwQze/ZsMiz43zJnzpyI00Tv6aefJiczRsvcoEg6smMm7Ztm8NSTT6bVl9PEiRP5y1/+Qu9OxoUnGdlZxqQPK1i3GdZthqcmlTPpwwo6tzMuOdko2rGZH/3oFvLz86OOLhF55ZVXWLliJc2PryCWtXuvUU5XI+9geOrpp9RDLbuJf76qR7q6W265hZtuuinqGAlj3LhxxDKzadZjEM0PPoZ1a9fot4tUKi8v57Zf38b2Ldu5adiP6Nmqd7Xbzz74PM7teyETJ07k2Wc17z4ZqHBMMBkZGZR7ReXldLZ8+XLenDSJL3TLICMcLhUzY1TvTD5duJCZM2dGnLBxrFy5knvuuZuu7Y1zjjOyMoPXYv1mp6QUSkphxfrgOgQ9j186CQq2b+X2238fZXSJSGlpKf994nFyOhs53fd8v+bHBF/szzzzTOOFk6SwadMmAB1U2EX8dRHYvHkzb0yYQPODjyYjpwnNew8hM7cpzz//fNTRJEFMnTqVhYsW8pV+X6d7y5413uesPucyqMNRPP6fxykpKWncgLLPVDgmmEMPPbTy8iGHHBJhkug9+OCDZGcaZ/TJrtZ+XNcsOjTN4MF//oOysrKI0jWeKVOmUFJSypnHGBmxus03atfSGN4P5s6dpx9+aWjGjBls3rSFpkc6ZsaWd5zSfCjNhw0vOlveCQ4yZDY3cvs448ePS4t/S1I3hYWFlasdzpgxI+I0iWn79u1RR4jcc889R2lpKa0HjQQglpVDy/4jeO+99/jss88iTieJIL4K/uCDhu7xPmbGUQcNZUfhDtavX99Y0WQ/qXBMMJ07d6683KlTpwiTRGvatGlMmzaNs/tk0iKn+ts0M2ZcfFgWS5ct56WXXoooYeP5/PPPadE0RvMm+7ZIRed2Vvl4SS8ff/wxlmHkdAmul24ALwlOJauD63G5PaCwsIilS5dGEzZimlezu8ceeywYqpqVycSJE/nkk0+ijpQQSktLKy9v2LChlnumvvz8fJ5/4QWa9xlGTuudv1taDzyNjJw8Rv/rX9GFk4TRvHlzALaX1H6gZXvJtmr3l8SlwjHBNGvWrPJyug5VLSsr4+9/f4CDmmdwWq/sGu8zqGMmA9pn8tijj7Jly5ZGTti42rRpw45ip6Ji3+Z0FoTbI7Vt27YBUomkBg2Nqm7cuHHBXKMmedCmNTRtwq2/+hWrV6+OOlrkqq78WLWITEePPfYYpaVltBt2frX2jJymtD7yLGZMn67tfoT27dsDsKm49iHem4s2k52do8IxCahwTDCZmZl7v1OKe/vtt1m1ajVfOiSLzJjxxEdFLN9azvKt5fzxvR088VERZsZFh2ezo7Aw5XsdjzjiCMrKnEWr9u1xnyytoHnzZvTo0aNhgknCOvzww/Fyp7gOu/sULYPcvFy6d69lMmQK0+IvO02ZMoV77rkH69oZWjTHYjFiI0ewtXAHt/zoR2k/vy87e+eBzNzc3AiTRGvp0qWMHTuOVv1PIbtlh91ub33EqWQ3a8M///mgevTTWElJCWPHjiUzlkn7vPa13rdTs06UlBTzxhtvNFI62V8qHBNMfF5JOps4cQLtmmQwsGNQRC/fWkFhGRSWwacby1m+Nfgi6tI8g8PbZTJxQmp/0BxzzDEc1LEDH3zqdV5JdtM257NVcNZZZ1f7sZNu0mnl3aqGDRtG8xbN2LGXvbgrip3iz41TR5xKVlZW44RLMIWFhUD6vlfiNm3axJ1//CPWvi0Zp5+8cx/HNq2wUaeyPj+f++6/L+KU0araO53OBxxGjx5NLCuHNoPPrvH2WGY2bYadz6JFC3n77bcbOZ1EraKigqlTp/Ld73yXadOm8aVDL6NpdrNaHzO8ywkc0uYw7rrrLv7whz9oT/MEpsIxwezYsaPycjpuiFpRUcHcOXPp3y5GrA4bTw/skMGq1WtSetuJjIwMvnTRxaza4KzZWLfHzFrkZGRkcN555zVsuASXrgtYZGdnc+qI0yheZnjZnguiomVQUeaMHDmyEdMllvhQ94KCgoiTRGv69OkUFxURO2E4tsvIl1j7dli/Q5n63tS0PrhZtQiaPHlyhEmis2jRIt577z1aDRpJZl4wrHDdO0+w7p3q+8G26Duc3DadefSxx9TrmCY2b97Mc889x3XXXsett97KjvxCvjvkJkb0PH2vj82MZXLD0Js5s88XmTJ5Ctdccw2/+MUveO+997RwW4LRuMgEU/UfSFlZWdrNc9ywYQOFRUV0bZFTp/t3bR4c+1i6dGlKz+U7+OCDASiqMh2ruDQYLjVq1CjGjh1LcenOH3SFxcHcyFR+Tfakaq9Afn5+2s6ZOOyww3jhhRco27rn+5RtCla069u3b+MFSzArVqwAYHl4nq7i/068YAfWts1ut3vBDrJzctK2Z7qsrIwxjz5KRruO0KIVz7/wAhdeeCGtWrWKOlqjeuaZZ8jIzqP1gFMr24o2LNvtfhaL0fqos1kx4UFmzJjBMccc05gxpZGUl5fz/vvvM3bsWKZNnUZZeRm9W/Xh6oHfYGino8mIVS8znvz4PyzcuIDCsh3kZTahb5tDubTfVwDIysji/EMu4pQep/HW0olMmfMm06dPp1XLVpx2+mmMGjWKbt26RfE0pQoVjgnGqvSyWR163FJNfOuIdk3q1hneNrxfqi/hHF8Sv0XTnW3FpTBq1Ci+9a1vATDx9Rcqb2vZDBYs38CSJUvo2bNnIyaN3rZt2yovp/rCSbWJH4Sy2v4phR8x5eXlaXeQCoLnPStcwGPtmjVs3rw57QqBuKFDh9KhY0c2zPgQ79al2m2+IR//bDHnXnxxWr5PAObNm8f6devIPu18rGUbij9fwJQpUzjnnHOijtZotm7dyttvv03zw04iI6fJXu/fvPcQNrz3FK+++qoKxxRTXl7OuHHjePKJJ1mzdg3Nc1pwcrfTOK7riXRp3nWPj1u4cQHrS9dWHvCmhlFULXNace4hF3L2wecyb/0c3l35Ns8/+zzPPPMMQ4YM4Wtf+xqHHXZYAz47qY2GqiaYqsNT03F4R3yobpPMuhXNTbKC+6XyMLPNmzfz9NNPcWh3o22Lna9LThaMHTuWBx54gLFjx5JTpSNgcF8jJ9t4+OGHI0gcrar/btLx31Dc/PnziWUZGbV0uGa1Deb2LViwoPGCJZAFCxZQVloKTYMRDum8Z2F2djZf++pXqdi4CV9ffauJik8/Iys7my9/+csRpYte5Sqq2TlYTvB+SbcVeadNm0ZZWRktDzmusm3dO09QnL+c4vzlLHvxzmpDVi0jk2YHH83MmTMr5xJL8isoKODmH9zMfffdR15xU6478tv84eR7uPjwL9daNAIUlu2oPOA9atQoCst27PG+GbFMBnUczLcG38jtp9zNuX0v5NN5C7nxxht5/PHH6/tpSR2pcEwwGzfuPPySjvtExRdyKS6v20IVxeH8rVRe4e6jjz6itLSMow6uXkznZAWLKb3wwgsUFRVVKxzzcoxDuzmzZ89Oy7mycenYaw9Bb+PbU94mu5tjGUZFSfBv5Pzzzyc3N5eK8PduTlewDEvb+VrvvPNOcKF5LrFmuUyZMiXaQBFbtSpYutliu/w0yIhRXl7OmjVrIkiVGPr3709uXh7lC+ZQ9skcIFiEKp3MmjWLzLzm5LTfuVJ30YZlVJQUUlFSSOHqT3cbttq0+xGUlZXx0UcfNXZcaSAvv/wyH8//mKsHfoMfDf8FQzsdQ2asbgMY8zKbVDvgnZe5955rCHohzz74PH570h8ZctAwxowZUzlCTRqXCscEU3Up4sWLF0eYJBqdOwcbCa/ZXreeovj9OnXq1GCZohY/0r2loO6rPro7WwvAvSLtCseqQ1WrXk4nM2fOZOuWreSFUxe9hGpHeT0sHGPZRk5PZ+KkiWm3L5278/aUtyEnE8zwnu2Z+X569ozk5+fz+9//nscffxzr0wt2meMYG9APcnP4/k03BfNm03CxiiZNmjDy9NOpWPIpFZ/OZfDgwWk332rhokXktO+1Twfkctv3BOCzzz5roFTS2OJ7M36wdgbrdqzdp8fmZeVVO+Cdl5VX58dWeAUL8j9m6dYlNMlrQpMmdSs6pX5pjmOC2bRpE3mZWRSWlabl0d327dvTvFlTlm/dOQSosNSrLQJTWLrzthXbgsKxd+/ejZ61sZx44ok899yzTJq1iA6tvdpw1T35cKGzeLXzjW9cnXbbcVRdYTcde+0BJk2aREZujNzuwb8Pyw6GNUNwblXmyjY5BDZ+tp3333+f4cOHRxE3Ep9//jlr16yFlsGPj1jvDpTNW8706dP5whe+EHG6xrFjxw6efvppnnn2WUrLyogNGUTsyCOomDoTzw9Gv5S9PA5r24bYeWdROvldHnjgAV586SWuu/Zajj322LTq1e/atSteXo5v35p2RSPA2rVrye3TZ58ek5HThKy85qxdu28FhiSuU045hfz8fB599FFmT/6Qw9sN4NguxzOww1HkZtb/6K8NO9YzffVU3lv5NusK1tK5cxd+8aOf06xZ7Vt8SMNQ4ZhAKioqKCkpoUV2DhaztCwczYyOHTuyeevSyrbCMq+2CMyUcS9W3rapqILcnBxatmzZ6FkbS0ZGBj/+8U+46abv89zkbVw2wmneZM8/1uYvreDNWc5xxx6blttxVJ3vWnV7m3RRWFjIe++9S07vCiwjeJ/EsqEoPzjKC5Ddeuf9c7pCRq4xadKktCocJ0yYADGD3HCM90GtiDXNZcKECWlROE6fPp2777mHTRs3Yr16kHH0YKxFuLJq/kYoCXqgfXXwg9+aNiFj1Kn4shWsmf4Bv/71rznqqKO4+eabadeuXWTPo7FUVFTwxoQJWFY2ZOcwecoUrrrqKvLy6t5jkswqKiooKiyk6S6L4pSXFFY7sFtesnuPfSynSUqvQ5BuzIyLL76YU089lZdffpnx48bz8Oy/k52RTf92Axl80FCOaD+IvKzdewS7Nu9e6/W4dQVr+WDNTD5YO4OlW4LRd/379+eqc77OSSedRGamypeo6JVPIAsXLqSiooK8zCy6NWnFB++/j7un1RFdCIZmNo/tfM55mVatt6R91s7bMmNGWVkZFRUVxHadl5NCOnfuzO23/4Ebbvge731UzshhNb8nSsucN2cZ/fodzk9++tO0XAFx6dLgoENmlrFkyZJow0Tgtddeo7i4hHaH1u3+lmHkHhwM27xm3TV06NChYQMmgG3btvHqa69hPdvjhcEIBosZFYcexLTp01m6dCk9evTYy19JXu+88w633XYbsbatyTj3TGId29fpcWaG9egWrLo6/1NmzfiQG268kb/99a8pvxrtSy+9xKcLFmAt20BmJpvy1/PQQw/xve99L+pokaooKeSsKgd2X55Q8zxh97pPtZDk0KZNG772ta9xxRVXMG/ePCZPnsw7U97hw9kzyYxl0r/dEQzrNJxBHQeTnRGMfIpvvVGTjYX5TF/1HjPWTGPF1mCu7CF9D+Gai67hpJNO4qCDDmqU5yW1U+GYQF555RUMaJ6dw/AuPXnww/eYPXs2Rx55ZNTRGo27s2bNWvp2qVI4ZhlF23b2luQ12VkMtc0zysrLyc/Prxx3n6p69+7NqFFn8uorL3PKUTV/CX+6wiksdq655pq0G6Ia99Zbb9K+IzRt7kybFmxYnsqLJ1W1Zs0axjw6htxuRvY+fMc2HQSFn1Rw33338dvf/jblD1Y98sgjFBYWkjH4CMrf2bmibOyI7lTMW8lf/vpX7vjDH1L2YNTzzz+PNWtG7Nwzsf04cm+xGBn9D6OiVUvyX32dd999l7POOqsBkiaGTZs28cgjo8no1puK0lLMIDZgMC+//DKjRo1Ki31QY7EYWdnZVFTZLxgglp1X7cBurOnu38NeWpw2PbPpKBaLMXDgQAYOHMi3v/1t5s+fz5QpU3jrzbeYPftDmmQ14bguJ3FarzNonbv7HrGf5n/C+MWvMm/9HBzn8MMO5xtf/gYnnHBCWhzITDap+a2YhGbPns3rr79Oq9w8Yhbj2K49aZXXhAf+9je2b98edbxGs3XrVopLSmibV8d9HMP7pcvqWj169KC8wiktg/atjOwsyM6Cru2D68Xh9M9027sxbuvWraxcuYqOXeCgLlBcXJI2i0yVl5fzu9/9ltLyYlqcuG9H9zObG82HOzNnzuS5555roISJ4c033+TVV1/FBnbH2lXfq8TysrHhBzNn9mz++9//RpSw4fXo0QMvKMCXrajxdi8pqbYKr9ew7YSXl1OxYBEA3bvXPNwsVTz11FMUlxSTOXwE8WMqWUNOIJaTy6OPPRZtuEbUunVrynZU3xs3I7v6YicZ2dULRK8op3THVlq3bo2kvlgsRv/+/fnGN77Bv//zb+644w6GHTeMicvG84vJt/DKohep8GDu/aaijfx55t38afrtLC9Zypcv/zL/+te/uPe+e7nwwgtVNCYo9ThGrKCggGeffZYnn3iCg5o2p1lW0EuUnZHJ9Ucey5+mTeI73/4O13/jeo499tiUPQIeV1xcDEB2HUdYxu+XbvtpOXDKUTHWbw5WTL3klOCFeH9B+u5bCLBlS/CjJjcXcvOqt6W6cePG8emnC2l9GmTWYQGlXTXpD8UrYPS/RjNixIiU/KE3b948/njXH7FOrYgdXfMiH3Z4Z2z1Jh599FE6derEiBEjGjllw7v66qtZ9NlnfDJhMr4+n9iwo6pvwVFSWm1e+QsT3qj2eN9eQMWEt/B1G/j617/OgAEDGjN+o5o4cSIvvPACGX0HEGu1s7fEsnOIDTqG6dPe4vHHH+eyyy5L+e/nLp0788nKfTtIW7p1A+4VKb3yudQsFotx5JFHcuSRR7JmzRoefvhhXpr8HB+smUHHpp2Ynz+Pcivn2muv5dxzzyUn3B9VEpsKxwi4Ox9//DFvvPEGEydMoKi4mOFdevL1QUdz77S3Ku83sGNnfnb86Tw0ayq33XYbXTp35oxRoxgxYkTKDsuMr5JVUFq3HpP4/dJlda34hPCSUmhaw+jLkrLq90s38Y3sm7WAZmFn0ieffJIWi77MnTuXzCYxcvvs38EDM6PpEU7+klIWLVqUcnvUffbZZ/z8F7+gomkOsZEDsYxYMEw1P9iypezFmVi75mQcfyixk/vhBcX88a4/0qRJk5R7/zRt2pQ/3nknf//733nllVfwggIyTjlx5xDl7Kxqww9purMXybcXUPHSWLIrKrj55z/nxBNPjOIpNLhly5bxyOjRvPfuu2Qc1JWsY3c/gJB5xDA8fx1jxoxh+owZXH/ddfTr1y+CtI2jV69ezJ47Dy8vwzLq9h1TnL+88rGSvg466CB+9rOfMXDgQF58/kXW+Eq69+7O92/6vt4bSSY9f11GZMWKFYwfP55JEyeybv16cjIzObpTd0b2OYxerdry2JwZLN0SLIH+27fH06Nla746cBi/P+Ucpq9ayhuLP+WRRx5h9OjRDOjfn1NPO42TTjqJpk2b7uW/nDyaNGlCyxbNWbu9aO93BtYWpP4+jlX1798fgCVrnNbNd+9VWrIG+vTpnTZz+qoqLy/n6aefpnkLo3VbxywYrvryy//joosuSvmDC3369GHixIkULoAmh+37473MKZgDsYxYyi0Ms2zZMn704x9THHPs7MFYXjCywzdsg5Jwn9PVm4kfrrKMGIwahL/8Ib/57W/43W9/l3JzzbOzs7nhhhto27Ytjz76KH7YIVjnYGKsZWdTlL+pcl65td65anX5h3PILC3lnvvuS8ltkNauXcuYMWOYOHEilplF5tATyRx0NBbLoOS9CVTkBz1uxS//F2vbgaxTziHWpQcLZrzNTTfdxNChQ7n66qvps4/bViSDww47jIrnnqNowzLyOtbt/33hmkVkZWerOBAAvvjFL/LFL34x6hhyAFQ4NoLNmzfz5z//mSlTpmBmHNGhExcMPo6hnbqTl5VVeb+lWzZRWBYsgf5J/s49jzJjMY7r2ovjuvZizfatvLdiCe8uXcK9997LP/7xD6644gq+9KUvpcyCFj179WLl0o/qdN8VWyto17ZNyhcFcd27d6d3717M/XwpRx5cvVd23SZndb5z7QWpN7SuLkaPHs2SJUs45kSY837QdvhAeHPsdv70pz/x85//PKVXmf3iF7/IzJkz+fDNDylZ47Q4FmI5wWdCVjsoDbe3zGobXK+qZL2z9S2jNN/59re/lVJzS1auXMkPb7mFgrJi7NwhWPO6HVSx7Ew4axAVL33AL375S27//e9Tckhm5ZDk8vK6PaCsnMyMDFq0aNFwoSLy8ssv8/d//IOyigoyBgwlc9AxWN7OLQU8fx2UBNMpKlYvJ0bQU5956EAyeh9G2Ucf8MGc6bz/ne9wySWX8PWvfz2lhq8OGjQIM6Ng+UeVhWNuu+6VvYo5bbuR2676fNcdy+cxoP8Asqr81hGR5JU6n2gJbMyYMUyZMoXzDz2C+0deyC3HnsqJ3ftUKxrr6qBmLbjgsIHcOeKL/OqkUXTNa8aDDz7IvHnzGiB5NPr0OZhV2yqoqMPy3Su3Q6/eqXdktzYXXvglNmypYOUue9vP+czJycnmzDPPjCZYhB5//HGefvppeh8CXXrAlo3BqXVbOGIIvPvuu9xzzz2U1/XHcRLKycnhN7/5DRdffDFFn8bY8GSMHZ847k7L4y0oGNtCu/OMlscHBWVFsbN5srPhOWha0Ypf//o2zj333IifSf1ZtmwZP/jhzWwtKsDOOQprtfu+YrWx3GzsnKMoy8vkpz/7GXPmzGmgpI2voqKCp556ivvvv59Yp45Yl7qN2sgY1J+isjJuuPFGPv744wZO2XjGjRvHn//8Zyo6dCH74mvJGn5KtaJxbywrm6wjh5N96fXEDhnAk08+yejRoxswceNr1aoVhx12OAWL369s63D8ZeS07UZO2250P+8WOhx/WeVtxRtXUrx5Dccdd2wUcUWkAahwbATNmweTrY7s2IXW+/BFVBsz4+A27ekVTtZPpeGqvXr1oqTcK4ehdmsRIy8T8jLhkDYZdGsRvG1Ly50128pTcrhUbY477jgyMmIsXr2zsHZ3lqw1hg4dlja9rxA873//+9+MGTOG7r1g0NDd73PwYUHP4+uvv87dd9+d0sVjVlYW1157Lffffz99uvdl85uw8X9G2dbdD8IULnY2PBmjcL5x3rnn8dCDD3HMMcc0fugGMn/+fG76v/9jS2EBds5grM3+/buwJjnYFwdTmpfJT376E6ZMqXmfumSydetWfvazn/Hwww9Dz+7EzhhRfXGcWlib1mScM5JNxcX84Ac/4Kmnnkr6PfpWr17N3x74Oxmdu5N1xpeINdv/3lTLySXrxFFkHDqQp59+OqUO6gKccsrJFOWvoGjDssq23Hbdd+tpBNiy4F1iGRkpOw9WJB2pcGxAxcXFTJ06tXLBjjXbt9X7fyP+N99++20WLVqU9F/gAIcccggAizYGP/Av659LtxYZdGuRwQ+PbcJl/YOhZos3l1PuzmGH7ceEriTWtGlTevfuzbpNO/9fFxbD1oKKlBxKtycFBQXcc889PPbYY3TvDUOOBYvB7JmweVNwmjw+uH74wOD0xhtv8Mtf/oL8/Pyo4zeovn37cu8993LjjTcS25RD/nMxYrnBEFV3Z8t7zqZx0L1TT/7yl7/w7W9/O6UOOLz77rv88Ic/ZEesHDtvCNZ2D8+tpKzathOVq0vtwprmYOcOpqJNU37z29/y/PPPN2D6hlVYWMgPbr6ZD2fPJnbCcDJOPQnbx9Ev1q4tsQvOxnt04+GHH2bMmDENlLZhlZSU8Nprr/G9G26gpKKCzBNH1VpAe0nxLtuUFNd4PzMja/gpxFq04ic//SlPPvkkBQUFDfU0GtWIESPIys5m87yJlW0djr+sWk8jQEVpMdsWTOHY4cNTcoVmkXSlOY71bPv27UyYMIHp06czZ/ZsSkpLycvK5rxDjmB41561PrawNNg7a9SoUYwdO5bC0r1vMfH1QUfz2NyZ/Pfxx3n88cdp26YNQ4YO5cQTT2To0KFJOb+iR48edGjfjhmrN3NiLduDzVhdRlZmJoMGDWq8cAmie/ceTH/vc1o2DXplN4bHJLp16xZhqoa3detW5s2bxwcffMAbb7xOYWERhw6AfoOo3F9ty0YIpwqzocrK8YcPhJxc+PD9D/jalV/jpBNPYtiwYQwcOJB27drt/h9LcrFYjLPOOoujjjqKX976S1YsX06bc51tM6BgNpxzzjl885vfTLm5RxMnTuTOO+/EOrTARg2qXAinRiVlu2w7MXaPd7W8bPjiYGzCPP7+979TUFDAFVdcUd/xG9yUKVNYtnQpGaedTKzX/u+/aDnZZJx6EuUTJvPkU09x2WWXJc2iXEuWLGH8+PGMf/0Ntm3dQkaHzmSNPJNYi1a1P7CkuNr75cUJk/Z4V8vOIeucL1P69jgeeeQR/vP445xy8smMHDmSfv36Je2aBM2bN2fk6afz6thxtBt2PplNW9V4vy0L3qGsqIALLrigcQOKSINS4ViPPvnkE26++WZKS0vp1LwlJ3frw1EHdeHwdh3JjO19UY4dZdX3znpn/Bt7eQR0aNqcHww/hS3Fhcxes4rZ61byzptvMX78ePoefDD33Htv0v0wNDPOPueLjB49ms82ldOn9e6v3aaiCt5ZUcbJI05LqWG6ddWnTx8mTJhAszzIiMHajV7ZnuwKCgpYv34969evZ/Xq1axYsYLly5ezfPky1q8PJnZmZBiduzkHHx7MY6yr3odAh07OovllTJkyiYkTg6PmrVu3pFu3HnTt2pVu3brRuXNn2rdvT/v27WnevHnS/siDYMXhO++4k29/59tseGEjVMDpp5/Od7/73aR+XjX5/PPPueuuu6BTK+zMI7GsvXzuZmfusu1E7V+JlplB7PSBVLz1MY899hh9+vTh2GOTa/5WmzbB9IaKZcuxrp32ubexms1bsI2baN68eVJ8z8yaNYvR//oXn8yfj8ViWLc+ZB8/kliXnnX7t5Cds8v7pfYhrdakGdlnfImK9asp++hDxk2YwNixY+nWvTtXfOUrnHzyyfXwrBrfRRddxKuvvsbG2ePocNylu93u5WVsnj2Oww4/PK1GwYikAxWO9ejDDz8MisZmLbhq4NEc1q4DMat7j1+TzOp7Z3XMztvLI3ZqmZPHST36MKRTN6auXMLo2dNYuGgR+fn5HHTQQfv8XKJ23nnn8fxzz/HU/O38+NjdX4fnPinGLcZXvvKVCNJFL74tR3EJNMmFZeucTp0OqvxRmMg2bdrEqlWrWLt2LevXr2ft2rWsW7eOdevWsG7degoLq2/FkpVl4b6MTv8u0K4DtGrr7O8Cqc2aw5FHw6ChzuZNQa/klk1bWLF6DgsWzKO4uPo+iDk52bRr146OHQ+iQ4cO1U6dOnWiffv2CV+AtW7dmq999Wvce++9AFx//fUJn3l/TJw4kfLycjJGDtx70QiQnUlR/vbKbSdo3WqvD7GYETvpcHzFRsaPH590heOQIUO4/PLLefzxx6lYuRqOPILYoQdjVf5BWds2eP7GysvWtvrnim8voGLWXHzBIpo2a8Yvf/mLhF+xeMGCBfz4xz+G7FwyjzmFzL7992nxGwh6EYvyiyrfL7HWddtPOda+E9knd8JLTqX88wWsnDeD22+/HXfnlFNO2denErnOnTszYsQpTHrrLdocdSaZedUL6C0L3qFkWz5XfOWmlPyckfTwwAMP8Pnnn0cdo8H07t27sqNqX6hwrEcXXnghBQUFvPzyy/z+nddpmp3DgPYH0b/9QRze7iAOalp7z0VeVjZFW3funZXXtOUe7xtXWl7OZ5s28En+WuauW83CjeupcKdL5y5ce921SVk0AuTl5XH1Nddw991388Ga6vOOlm0pZ+rKMi655JK02b9xV4cccggtW7agsGgreTmwfJ1x9jmJu7DJsmXL+PWvf8369espLq4+LygnN0ZeEyevidO5O+Q1hSZNwvOmkJvn7Mtvj9JSqg35Li2teU9QiwW9ldV7LCsoLoKC7VC4AwoLYEdBCYU7VrF46WrmzzcKC3cvLHNz8/jlL3+Z0EfXhw0bBkBGim6lAFR+3lXMXUZscK9gP8Z65u74wjVU7ChJ2s/XK6+8kqFDh/LPB//JJ+9Mg1nzYGA/Yof1xTIzyTh2WGXhmHnOGZWP863bKJ89Dz79DDPjzFGjuPLKK2nVqlVEz6TuKqdtVJTh27dSsWEtsYO6YFm1DGWuR15eTsXG9fi2zZVj6RO92K7N5ZdfzsSJk9g4axwdjr24st3Ly9g06zUOOeRQhg6tYbUyEUlqKhzrUU5ODtdeey1XXHEF06dPZ8aMGcycMYNps5YC0DI3j0PbdODwdh0Z0KHTXgvJmpRVlLNw4wY+Wr+aT/LX8dmmDZSWl2Nm9O7Vm0tOH8Gxxx7LoYcemvRH+k477TSefupJXv1sLbkZDgTPZ+znJTTJy+PSS3cfIpMuYrEYw4cfy/jx4ygsgbJy57jjjos61h599NFHrFixolpbm/bQtj00b1lBXh7khqfsHPapUNxVaQnVhnyPf/2FfXp8Tm5wAnAP/l5RIRQVOUU7nO3bIH895K+DigooLi6huLiEqVOnJnTh2LZtWy699FL69esXdZQGM2rUKObNm8ekSZPwz9bhA7tjfQ+qW+/jXnh5Bb5kPcxeRsW6LQw44oiknOMY179/f+69514++OADHn/8cea9NwPmfowNOwrr06taL6OXlFDx/mz84wXB3Nmzz+biiy+mY8eOET6DfdO3b1/uvvtunn76aWbMmEHJR+9jsRixdh2hQ2di4cmataiX707fUUDFulWVJ1+/Bi8rJRaLMXDQIC44/3yGDx9eD88sGl27duXkk7/A5Clv0vaoM8nIDRag2rpoGiVbN/CVH3wv6X+DSHrbn964dKDCsQHk5uZy0kkncdJJJ+HurFy5kjlz5jBv3jzmzJ7N9DnTgWB+4jFdevCF7n04qFkLerRszdItwVHeHi3b0KNlsBKZuzNn3SreXvY5s9atpKi0lJgZffr04ZwTj2PgwIEMGDAg5XoRMjIyOO/8C/jLX/5C9xYxcjNhW3EFH6wp54vnnpNSq0Duj2HDhjFu3Di2FQS9XolctJx55pkMGDCASZMmsWzZMtauXcO6detY+PGW3e4bi0FuXoycXCcn1yt7HquecvP2XFxmZVNtyHdOLSO+K3sXC2BHlVNxkVFcZBQWOhXlu69U3Lx5M3r16kCHDh3p0qULX/jCF+jbt+9+vTaNxcy4+uqro47RoDIzM/nRj37EF77wBR597FE+nzyf2NRFVBzcgdihnaHDvhcFvnE7FZ+uxj5dQ8WOYjoe1JHLb7qa008/Pal7jCB4TwwZMoQhQ4Ywa9Ys/vngg3w2aQq2ZDkZJx+PZWbi+RupeP1NKrYXcOaoUVxxxRVJu5hUv379uPXWWykqKgq+j+fM4aOPPmLBp3MpnRfsTZjRtBneoTMZHbsS69wda7NzKLq17QBbNgEQa9k6uE7YC711ExWrllGxZgWsW0X51s3B/TIy6NOnDwOGn8MRRxzBwIEDK7foSnaXXHIJkyZNYvP8t2l71Jm4O5vnvE73Hj1TamsfEdnJUmH7hvowdOhQnzlzZqP8t1atWsX777/P1KlT+eCDD8CdU3r05csDBnPXe8EqbT8/cSQAy7Zs4sFZ77F4Uz7NmzXjhBNP5Oijj2bQoEFpsSjM9u3buezSS2maUU6HpjEGH5TJEx8X88ADD6Td/o272rx5c2Wv6+CjjuL2P/wh4kT7rqSkhPz8fDZs2MCmTZvYtGkT+fn5lZc3bFjPunXrKCjYUe1xeU1itG1fQZce0GWXhSFnz4QlC4PewuYtoV3H6vs7rl8Lyz6H/HUxtm+rPuw0Ny+XDu3b065de9q0aUPr1q2rnbdt25Z27dolzeqR6czdmTdvHq+99hqT336b0pISYq2bwWGdsMM6YzlZlL+zAN+wc5ska9ecjOMPxcvK8UVr8Pmr8LVbiMViHH300Zx55pkMGzYs6QvGPSkvL+eZZ55h9OjRWJdOxI4dRsVLY2nVrBm/+PnPU7a3uqysjMWLFzN//nzmz5/P3HnzWL8uWJI5ltcU696bjIP7E+vUrdqBh4oNaylbOA+WLqJ8W3AQrEWrVhzRvz+HH344hx9+OH379iUnJyeS59UYbv7hD1mwZBU9v/x7itYuZtkLt3PjjTdy1llnRR1NRPaTmb3v7jWONVfhGGrMwrGq/Px8nnzySV566SW6tWhFdiyDzFgGPz9xJO+vXs5fZr5Ns2bNueqaq4P9k5Jg5br6dvvttzP5rTfp0ypGYXmMvA49+Mtf/xZ1rIRw1llnUV5ezpe+9CWuv/76qOM0mB07doQL6Kxj9erVfPzxx0yd+h5FRcWcPAra7NIBMnl8cH7SyOrthTtg/ItGRQUce+yx9OvXjy5dutCxY0c6dOhAs2bNNLwqBRUUFDB58mReGzuWBZ98EgxdPbwLsaN6Vtuuw0vL8bnLYM5yKopK6NqtG2edeSYjRoxIq73oXnnlFe6//34AmjZrxt/++teknc+5v9avX8+sWbOYMWMGU6dNo7ioiIz2B5F5wkjIyaNsyjjKVywhIzOTIUOGcPSwYQwePJjOnTun1WfIhAkTuPPOO+l23o/Ytmg6BQvf4aknn6RJk31beEhEEkdthaOGqkasbdu2fPvb3+boo4/mt7/5DZSVc3Tn7kxdsYS/vj+FQ/r25de33ZZWP1p2deaZZ/Lmm29SVA4rtpbxvSt1JDMuFotRXl5O586do47SoJo0aULPnj3p2bMnEKy6O2PGDH7+85+zekWwwE1dfqttWAvl5c51113HRRdd1LChJWE0bdqUM888kzPPPJPPPvuMZ599lokTJ+IL1+Cn9CPWvR2+YSv++jwqtuxg2LBhXHLJJRxxxBFpVQTEnXXWWfz73/9m48aNXHzRRWlXNAK0b9+e008/ndNPP52ioiLeeustRo8Zw6bnHwUgN68JV117LaNGjUqZoaf7Y/jw4WRkZLJ9ySwKls7i6GHDVDSKpDAVjgli6NCh3HHnnfz4Rz9iyvLPmbz8cwb0789vfvtb8vLqvi1HKho4cCDt27Vj+YYNZGZmJO3eVw0hOzub0tLSpJ1zdCAGDBhA125dWDBvJauXG116ON17Q9Nm0LLK7gFFhbBiCSxfYmzKd1q1askJJ5wQWW6JVp8+fbjlllu4+OKL+cMdd7Dktdn4YZ1h0VratGzFLXfcypFHHhl1zEiZGVdddRUv/e9/jBgxIuo4kcvNzeWMM87g6KOP5qWXXqK8vJyRI0fStWvXqKNFrmnTpvTrdzgfzZ9MRUkhQ4YMiTqSiDQgFY4J5NBDD+XG73+f22+/HYBf3npr2heNEPSqHTN8OC+//DL9+vVP+0VxqmrZsiUFBQVJsRx+fcvLy+Mff/8nEyZM4PXXxzNv7jzmz4EOnWDAUcEiOdPfhlXLg9VPe/fpxSUXnc6ZZ56pf1dCr169uPtPf+L/bv4BS+YvpnXbNtxz991JtVJoQxo5ciQjR47c+x3TSOvWrbnyyiujjpFw+vXrx9y5cysvi0jqSunC0cxGAfcBGcBD7p7wq4eccMIJnHTSSQwaNCjlVkk9EH369AGCQkl2is9RTtehQZmZmZxxxhmcccYZrFu3jjfeeIPnnnuWia9uByA7J5sLLvgiZ5xxBj169Ig4rSSapk2b8re//JWCggLy8vLScg65yIE6/fTT2bBhA61atdLnrEiKS9nC0cwygL8CpwMrgBlm9pK7fxxtstplZmbys5/9LOoYCSe+Kl3lJs4CsHOZ+DSch7WrDh06cPnll3POOefwy1t/wfZt2/n1r2+jS5cuUUeTBJaRkaGDdCIHoFu3btxyyy1RxxCRRpCyhSNwNLDI3T8HMLMngPOAhC4cpWbdunUDYPDgwREnSSwDBgxg1apVKb3c+75q0aIF995zX9QxRERERFJKKheOXYDlVa6vAKrtSGtm1wPXA3TvvstmcJJQDjnkEB599FE6dOgQdZSEct1113HMMcfodRERERGRBpXK4/5qGrtXbdNKd/+nuw9196Ht27dvpFiyvzp27Kghmbto0aKFVggVERERkQaXyoXjCqBbletdgVURZREREREREUlaqVw4zgD6mlkvM8sGLgNeijiTiIiIiIhI0knZOY7uXmZm3wXGEWzH8Yi7fxRxLBERERERkaSTsoUjgLu/CrwadQ4REREREZFklspDVUVERERERKQeqHAUERERERGRWqlwFBERERERkVqpcBQREREREZFaqXAUERERERGRWqlwFBERERERkVqZu0edISGY2XpgadQ5Qu2ADVGHSEB6XWqm16Vmel12p9ekZnpdaqbXpWZ6XXan16Rmel1qptelZonyuvRw9/Y13aDCMQGZ2Ux3Hxp1jkSj16Vmel1qptdld3pNaqbXpWZ6XWqm12V3ek1qptelZnpdapYMr4uGqoqIiIiIiEitVDiKiIiIiIhIrVQ4JqZ/Rh0gQel1qZlel5rpddmdXpOa6XWpmV6Xmul12Z1ek5rpdamZXpeaJfzrojmOIiIiIiIiUiv1OIqIiIiIiEitVDiKiIiIiIhIrVQ4ioiIiIjUIzNrbWYDo84hicnM7qhLW6JR4SgJy8zam9ldZvaqmU2Mn6LOFSUzu9jMmoeXf25mz5nZ4KhzJYJk/RBuSGZ2vJk1DS9fYWZ3m1mPqHNFzcwyzOyPUedIVGbWwcy6x09R50kEYRFwtJmdFD9FnSlKZvasmZ1tZvodWYWZvWlmLcysDTAbGG1md0edK2pmNtPMvmNmraPOkkBOr6HtzEZPsY/0Dz5BmFmWmd1gZs+Ep++ZWVbUuSL2H2A+0Av4NbAEmBFloATwC3ffZmYnAGcAY4AHIs6UKJLyQ7iBPQDsMLNBwC3AUuDRaCNFz93LgSFmZlFnSSRmdq6ZLQQWA28RfOa+FmmoBGBm1wKTgXEE30XjgF9FmSkBPABcDiw0sz+Y2WFRB0oQLd19K3AhMNrdhwCnRZwpEVwGdAZmmNkTZnZGun7+mtm3zGwucKiZzalyWgzMiTrf3qhwTBwPAEOAv4WnwaggaOvuDwOl7v6Wu18NDI86VMTKw/OzgQfc/UUgO8I8kUv2D+EGVubB0tnnAfe5+31A84gzJYoPgRfN7KtmdmH8FHWoiP2G4DP2U3fvBZwKvBNtpIRwIzAMWOrupwBHAeujjRQtd3/D3b9C8FtlCfC6mb1rZlel+UHvTDPrBFwCvBx1mETh7ovc/WfAIcDjwCPAMjP7ddg7m04eB74IvBSex09D3P2KKIPVRWbUAaTSMHcfVOX6RDObHVmaxFAanq82s7OBVUDXCPMkgpVm9g+CI5h3mFkOOgD0OEGvyO3Aj6u0b3P3jdFEShjbzOwnwBXASWaWAaTzj7qq2gD5wIgqbQ48F02chFDq7vlmFjOzmLtPSvfh3qEidy8yM8wsx90/MbNDow4VNTNrS/DZ8lWCAzH/AU4ArgROji5ZpG4j6JGe4u4zzKw3sDDiTAkhnO95FXAW8Cw73y8TgSOjS9a43H0LsAX4cjh6rK+7jzazdmbWy90XRxyxVtrHMUGY2QfAxe7+WXi9N/CMu6ft/DUzOwd4G+gG/BloAfza3V+KNFiEzKwJMAqY6+4LwyObR7j7+IijJYRdP4SB5on+IdyQzOwgguFkM9z97XC+2snunvbDVWV3ZvYGcD7BQZh2wDqCg5rHRZkramb2PMEP3u8THGjYBGS5+1lR5oqSmT0HHAY8BvzL3VdXuW2muw+NLJwkHDN7H9gMPAw86+7FVW57zt3TbrSHmd0KDAUOdfdDzKwz8LS7Hx9xtFqpcEwQZnYqMBr4HDCgB3CVu0+KNJgkFDO7i2DexEdRZ0k0yfoh3FDC3sVx7q75NVWY2S3ufqeZ/Zmgh7Ead78hglgJIVxIqZBgFMNXgJbAf9w9P9JgCcTMvkDwuox195Ko80TFzEa4e1ovVlcTM7sT+C3Bv6OxwCDg++7+70iDRczMerv751HnSCRmNotg2PsH7n5U2DbH3RN6JV4NVU0Q7j7BzPoChxIUjp9UPSKTTvTDrlafAP80s0yCAw3/DYc9CFxA+CEM4O6rLFyBNh25e7mZ7TCzlnqPVDM/PJ8ZaYoEEx5oeDE80FBBsPBWWjOzFu6+dZc5WHPD82ZAOg+Ff8vMzgV6UuW3pLun+wqiI939FjO7AFgBXAxMAtK6cAQ2mtkN7P5+SeffcyXu7mbmUHngLuGpcIyYmbUAOrr7QncvDudN5AGDzGycu6+NOGIU9MNuD9z9IeCh8H1yFTDHzN4BHlTvdHJ+CDewImCumb0OFMQb0/nL2t3/F55XK4zMLJdggYK0pAMNNXocOAd4n+AgZtVVIB3oHUWoBPE/ws8XggMNEojPIT+L4MDuxjRdPHRXrwJT0fulqqfCNStamdl1wNXAgxFn2isNVY2Ymf0TeNfd/xVeX0iw0EcTghURvxlhPElAYc/AOQSFYzfgKYIJ5gXuflmU2aJkZjcDfQm25bid4EP4cXf/c6TBImRmV9bUvmvRlK7Cf0sjgS8TbG/ztrtfFG2q6JjZUwSrqupAg9QqGYbURcHM/kAwT7gQOBpoBbzs7sdEGCtyZvZBOq/ZsSdmdjrBd5ARTC15PeJIe6XCMWJm9iEwOFwyHzP7sMpY5ynufkKkASNgZv+jhiGqce5+biPGSSgWbCR8LjABeNjdp1e5bYG7p/VKf8n4IdzQzCwP6O7uC6LOkigs2Lz9coJtbaYDxwO93X1HpMEipgMNNTOz44FZ7l5gZlcQbEFxr7svizhaZMLVdidoYbbdWbDJ/dawF78pwSJta6LOFSUzuwnYTrBFSeU0LK18nnxUOEbMzOa6+xFVrg9w93nh5XnuPiC6dNEIFx+AYAPdg9g5N+DLwBJ3/2kkwRKAmV0NPFHTD1wNMZNdmdkXgbuAbHfvZWZHArel+cGXFcAygn1yX3D3bWa2ONy3UGQ3ZjaHYJGTgQSriD4MXOjuX6j1gSksnMP3b4KFlEoJDta5u7eINFjEwpXP/4/gYN318bUr3D2t93Q0s+8AvyNYWTVeeLi7p91w73inkJlto+ZOknzgj+7+t0aOVicqHCMW7tV4xq5Ho8ysC/BaOg8FMbPJ7n7S3trSTXg0sy+QG29z98nRJYpWLR++EBzZ/Az4mbtPaLxUiSFcAn0E8GaVkQzVDlalGzO7j2Ao2VyCOWwvEmxvk3Y/YHYV/si9HehH9c+XtH5t4sPszOyXwEp3fzjdh96Z2eeE/45cPyQrmdmTBHNiv+buA8IRH++5+5HRJouWmX0GHOPuG6LOkugs2B/13UQdQZbuG4cngj8C/zOzk8yseXj6AvBCeFs6ax/uZwmAmfUC2keYJ3Jmdi0wmWCD4V+H57+KMlPU3L25u7eo6UTQY/0N4L6IY0alrIZe6LT+kefuNxKs7Hc3cArwKcFnzSVm1izKbAlgNEFPbBnBa/MoQQ9buttmZj8h2Oz+lXBubNZeHpPqFgLzVDTupo+730nQC4u7F1J9UaV09RGQ1lMBdmVm3Ws6hdsfnRx1vj3RqqoRc/d/m9kGgn1/+ofN84Bfuvtr0SVLCDcBb4ZHNiH4sfeN6OIkhBuBYcBUdz/FzA4jKCAFMLMTgL7uPtrM2hHMLZkdbu2SjuaZ2eVARtibdAPwbsSZIhf+2J0ITDSzLGAUwVD4vxFsfJ+u8sKtoczdlwK/MrO3gVujDhaxSwnmxF7j7mvMrDs6sLua4Pv5NarPWUv37ThKwl7G+LoVfajy+qSxcmCWmU2i+vslnRfeeqXK5VygF7AA6O/uq6OJtHcqHBOAu48l2ChWqnD3seGP3cPCprTd27KKIncvMjPMLMfdPwm35kh7ZnYrMJRgL9TRQDbBHJzj3f0fUWaL0PeAnxF8Uf+XoIf6N5EmSiBmlg0cAiwGrkTfiUVmFgMWmtl3gZVAh4gzRS6cSlK1IOoOHEPQI5uuFoen7PAkgVsJfs91M7P/ECy89fVIEyWGF8KThHadMmJmg0mCzhHNcYyY7dzs/v6abk/zozGY2XHsvmFs2n5Zm9nzBNtwfJ9g7tomIMvdz4oyVyIws1nAUcAHVebzacl4qZGZnUywyf0SgqFk3YAr03y+8DCCfXRbERxgaAHc6e7TosyVCMKFpS4HLiEomJ51979EGioBmFlzgk787VFnSRThHLXhBJ8rUzWvL1DlQB3AAncvjTJPIkqGudPpfnQ1EcQ3u38/0hQJyMweA/oAswiGOUAw/CNtC0d3vyC8+KtwyEdL1FsdV+LubmbxIUJNow4UFTO7192/v6etbdJ5VdUq/gSMjG9TYmaHEPTKDok0VbR6uvsMgmXzrwIws4uBtCwcw/fEZQTDmPOBJwkOuJ8SabAEYGYDCOa/tgmvbyBYEOajSIMlhlyCg7qZQD8zS+sF7KDmA3Vmlu4H6v6vytUYwTY/6yOKU2fqcZSEZWbzgX6afL+Tmd0GvE2w4lbB3u6fTszsZoLVZk8nWBnyauBxd0+7+Y1mNsTd36+ytU017v5WY2dKNDX1Rqd7D3VNR7uT4Qh4QzGzCoLP22vcfVHY9nm6rzILYGbvEqxWPSm8fjLwe3c/LspcUQv3t7yUYDGYirDZ0/1gXbjC9+W7Hqhz97Q9UBdOr4krIyiqn3X3omgS1Y16HCO2px6BuDT/sJlHsCpmwk4SjsASgqPf94fbULwNTHb3FyNNlQDc/S4zOx3YSjDP8Zfu/nrEsSIRFo0ZwHXufkXUeRLUTDN7mJ2rhl5Bmo78MLMzgbOALrtMm2hB8IMmXX2JoMdxkpmNBZ5AK2TGNY0XjQDu/mY6j/Ko4nyCfRvTfT2GXWXFi0YAd/80XJgsLYXfz83c/YdRZ9lX6nGMmGmz+z0Kh2IeCUyn+ipc6VxMA2BmBxHMtbkZaO3uzSOOFLlwu5bV8aN14cp2Hd19SaTBImRm44AvuntJ1FkSjZnlAN8hWLzCCLa5+Vs6vlZmNojgs/Y24JdVbtoGTHL3TVHkShRhQXQ+wffyCIIhd8+7+/goc0UpnG//AdUPvAx19/MjC5UAwlVmL9acz+rM7BGCTpL4++UrQKa7XxVdqmiYWaa7l5nZBHc/Neo8+0qFY4IwbXa/Gw2z252ZPUSwOfdagt7GKQSLwaRzrwAAZjYTOC7+wz+ciP+Ouw+LNll0zOwfBPMmXgIqhzan85L5ZnYe0NXd/xpen06wP6wDt7j7M1Hmi5KZZcUXrDCz1kA3d58TcayEYmZtgIuBS919RNR5ohK+P34NnMDOAy+/0kEGexYYBExA205UqnKgrur75W/p2DMbH/5vZn8imF7zNNW/n5+LLFwdaKhq4mhvZr3d/XPQZveQ3gViLdoCGcBmYCOwQUVjpcyqvUXuXhIWj+lsVXiKAWnfKx26hWD4YVw2wYI4zQi2cUnbwhF43czOJfhtMAtYb2Zvufv/1f6w9OHuG4F/hKe0FRaIaV0M7cFL4UmqCAvEu6m+rU26a0Ow6NYIggOXFp6rcJQ60Wb3oXDuXk1d4UYwybxFI0dKGPFVVc3scOAMgrk3Ge7eNdpkCWG9mZ3r7i9BZc9S2i6DHs6h6Ks5jrvJdvflVa5PCYuBjZqjRUt332pm1wKj3f1WM1OPo+wmXNzkZnbfLitte2EB3H1M1BkSkZkdD/wK6EH190s6LjTVIVxRdR47C8a4hB8GqsIxQWiz+500X2/PzOwc4ETgJKA1MJFgyKrAN4H/mNlfCD6IlwNfizZSdNy93Mzam1l2Os7bq0Xrqlfc/btVrqb1KA8g08w6Ecyf/lnUYSShPQ38HXiIndtlpS0ze8rdLzGzuVT/8R8/4J22qzWHHiboIHkfvV8yCEa41LTQlgpH2SdD2Hn0blC490/a7lkoNTqTYG7Afe6+KuowicTdPwOGm1kzgvnb26LOlACWAO+YmeY47jTNzK5z9werNprZNwgW4kpntwHjCHphZ5hZb2BhxJkiFfbcj3P306LOkmDK3P2BqEMkkBvD83MiTZG4trj7a1GHSBCr3f22qEPsLy2OkyD2tNl9uk+olp30A6ZmZnaFu/97l810K6VzkbTLPlGV3P3XjZ0lUZhZB+AFgoUrPgibhwA5wPnuvjaiaJKgwgMvX3X3LVFnSRRm9itgHfA81ReB2RhVpkQQDncvdPeKcDjvYcBr8UWn0pWZ/YGgp+05qr9fPtjjg1KUmX3o7kdFnWN/qccxcQxFm91LLcKhhzvMrKV+wFQTn5emIc67SOcCcU/cfR1wnJmNAPqHza+4+8QIY0XKzG5x9zvN7M/UMFRKBzApAuaa2etU77lP59flyvC86j50DqTjnLWqJgMnhqvOTgBmApcSbD+Rzo4Jz4dWaXOChWHSTdJtwVGVehwThJk9Ddzg7trsHvWu7YmZPQUMB/QDRvbKzNoTrCLaH8iNt6f7AhZSnZl9RjAf+OCabk/3BT/M7Mqa2tP9dZHdVdlq4XtAXnhAJql7mESqUo9j4mgHfBzuKZb2m92rd22PXglPsotwPtZ9BIW1A+8BN8W3uElT/wGeJJh3802CXoL1kSaSRPRn4C6gE8H75b/uPivSRAlEBeLuzCwL+BbBQm0AbwL/SPchmYCZ2bEEPYzXhG1p/1vbzFoCt7Lz/fIWcJt+3yUf9TgmCG12vzv1rsm+MLOpwF+B/4ZNlwHfc/dj9vyo1GZm77v7EDObE1/VL9yXr8bPG0lvZtaD4N/NZQQ91P8lKCLTcoGcWlbKBCCdV8o0s4eALCBeVH8VKHf3a6NLFb3wt9wPgHfc/Y7wgOb30/13i5k9S7D9RNX3yyB3vzC6VLI/VDhKwtLwoJ30A2bvzGzarkWimU119+FRZYpa/Pmb2TjgfmAV8Iy794k4miQ4MzsKeAQY6O4ZUeeJgpl1cvfVYUG9G3df2tiZEoWZzXb3QXtrEwEws1nufuTe2iTxpX33edS02f2epWOBWAst9b13k8zsx8ATBP+mLgVeMbM2kLar/f02HCL0A4LhiC0I9tIS2U04/HAUQY/jqQTDydJ2gaX4mgO7FojhZuaXA9+JIleCKDezPuE2SPGpAum+Px9mNomaD+6m+7zyQjM7wd2nQOW/ocKIM8l+UI+jJBz1rtVd/AeMu6fzDxgAzGxxeDH+nqm6ua67e7qv9idSIzM7HfgycDbBXpZPAC+4e0GtD0wjZnYkQbF4CbAYeM7d/xxpqAiZ2anAaOBzgs/aHsBV7j4p0mARM7MhVa7mAl8i2PPylogiJYTw388YoGXYtAn4urvPjiyU7BcVjpJwNDyodvoBU52ZDQOWu/ua8PqVBF/WS4BfpWlPIwBmNga40d03h9dbA39y96sjDSYJJewleRx4Np3/vewq3IfvMoKiOp9g4aCb3b3G76Z0Y2Y5wKEEheMn7l68l4ekJc0r38nMWgC4+9aos8j+iUUdQGRXVYcHVT0BXQm2Fkg7ZnaImf3SzOYDfwGWExz4OSWdi8bQP4ASADM7Cbid4MjmFuCfEeZKBAPjRSOAu28CtCy8VBN+jjyoonE3nxAM2f2iu58Qftam/XBMADP7DsF2E3PCXqMmZvbtqHNFzczaVDm1M7MzgIOizhU1M/u9mbVy963uvtXMWpvZb6POJftOhaMkNDM70szuNLMlwG8JvsjTkX7A7FlGlR+8lwL/dPdn3f0X7GFfujQSC3sZgeBHDZrbLlJXXwLWEMyffjAcnml7eUy6uK6Gg1LXRRcnYbwPzAzP3yOYX35NrY9ID2fW8H45K7o4sr/0A0ISzh6GB5m7nxJpsGh9ieA1mWRmYwnmIOkHTCDDzDLdvYyguL6+ym3p/hn3J+BdM3uGYO7nJcDvoo0kkhzc/XngeTNrCpxPsLBURzN7AHje3cdHmS9iMTMzD+c7mVkGkB1xpsi5e6+oMySoDDPLiQ9nNrM8ICfiTLIfNMdREo6ZVQBvA9e4+6Kw7XMtbgJVfsB8GRhBMCQzrX/AmNnPCI5cbgC6A4Pd3c3sYGCMux8facCImVk/gveKARPc/eOII4kkrbDX/mLg0nReKdPM/gj0BP5OcFDqmwRzzX8QZa4ohesyFLj7BjMbDpwALHL3F6JNFj0zuwU4l2BBJQeuBl5y9zsjDSb7TIWjJBwzu4Cgd+04IN679pCO5FWnHzA7hV/SnYDx8ZUgw57rZu7+QaThRERSjJnFgG8QjPIwYDzB93RaTqEws18AXycoip4ATgPeBI4BZrv796PKlijMbBTB62IE39XjIo4k+0GFoyQs9a6JiIgkpnC4YXd3XxB1lqiZ2cfAkUATYBlwkLvvMLNMYJa7D4gyXyIIe2T7uvsbZtaEYH2CbVHnkn2jxXEkYbl7gbv/x93PIVhRdRbw42hTiYiIpDczO5fgO3lseP1IM3sp0lDRKnL3knABmM/cfQdAOPe+JNJkCcDMrgOeIVgFHaAL8EJkgWS/pfvCEZIkwlUz/8HODx0RqYNdjvLmAZk6yisiB+hW4GiC4Zi4+ywz6xlloIi1MrMLCYZhtggvE15vueeHpY3vELxfpgG4+0Iz6xBtJNkf6nEUSSJmdkdd2kSgxqO8XdFRXhE5cGXuviXqEAnkLeCLwDnA5PBy1evprtjdK3tewyG8miuXhNTjKJJcTgd+tEvbmTW0iYCO8opIw5hnZpcTbLPQF7gBeDfiTJFx96uizpDg3jKznwJ5ZnY68G3gfxFnkv2gHkeRJGBm3zKzucChZjanymkxMCfqfJKwdJRXRBrC94D+QDHwOLAF+H6UgSSh/RhYD8wlWI33VeDnkSaS/aJVVUWSgJm1BFoDt1N9gaBt4fxPkd2Y2Z3AZuBrBD/0vg187O4/izKXiIiIJB8VjiJJxsxOIFjsZLSZtQOau/viqHNJ4gn3WrsGGEmwSMM4gr3W9MEvIiIi+0SFo0gSMbNbgaHAoe5+iJl1Bp529+MjjiYiIpLWzOxiYKy7bzOznwODgd+6+wcRRxOpF1ocRyS5XAAcBXwA4O6rzKx5tJEk0YTzYfd4VNDdBzZiHBGRdPELd386HBl0BnAX8ABwTLSxROqHCkeR5FLi7m5mDmBmTaMOJAnpnKgDiEjqMrNeBPOme1Llt6S7nxtVpgRRHp6fDTzg7i+a2a8izJMQzGwo8DOgB8H7xQDXQczko8JRJLk8ZWb/INhs+DqC+WsPRZxJEoy7L41fNrODCLbkcGCGu6+JLJiIpIoXgIcJtlSoiDZKQlkZfkefBtxhZjloBwOA/wA/JFhVVe+XJKY5jiJJJtwDaWR4dZy7vxFlHklcZnYt8EtgIsER3i8At7n7I5EGE5GkZmbT3F3DL3dhZk2AUcDccN/cTsAR7j4+4miRMrMp7n5C1DnkwKlwFEkCZraNnXPWbJebi4DPgJ+5+4RGDSYJzcwWAMe5e354vS3wrrsfGm0yEUlmZnY50BcYT7CXIwDpvgiMmd0FjHb3j6LOkkjM7FTgy8AEqr9fnosslOwXDVUVSQLuvscFcMwsAxhAMBRkQKOFkmSwAthW5fo2YHlEWUQkdRwBfBUYwc6hhx5eT2efAP80s0xgNPBfd98ScaZEcBVwGJBF9feLCsckox5HkRRhZt9w939EnUMSh5k9SvAD70WCL+nzgOnApwDufnd06UQkWZnZJ8BAdy+JOksiMrNDCYqlLwPvAA+6+6RoU0XHzOa6+xFR55ADpwm7IilCRaPU4DOCRSziRwhfBFYDzcOTiMj+mA20ijpEIgpHAR0WnjYQvFb/Z2ZPRBosWlPNrF/UIeTAqcdRREREROrMzN4EBgIzqD5nLa234zCzu4FzCebyPezu06vctiBd55eb2XygD7CY4P2i7TiSlOY4ioikGDO7192/b2b/Y2dvY6V0/3EnIgfs1qgDJKh5wM/dfUcNtx3d2GESyKioA0j9UI+jiEiKMbMh7v6+mX2hptvd/a3GziQikg7MrDXBirO58TZ3nxxdouiZWfea2t19WWNnkQOjHkcRkRTj7u+HF4909/uq3mZmNwIqHEVkv+2yRVQ2wWqZBe7eIrpU0Qv3zr0R6ArMAoYD76HVZl8heL8YQUHdC1gA9I8ylOw7LY4jIpK6rqyh7euNHUJEUou7N3f3FuEpF/gS8JeocyWAG4FhwFJ3PwU4ClgfbaToufsR7j4wPO9LMGx3StS5ZN+px1FEJMWY2ZeBy4FeZvZSlZuaA/nRpBKRVOXuL5jZj6POkQCK3L3IzDCzHHf/JNyaQ6pw9w/MbFjUOWTfqXAUEUk97xJsu9EO+FOV9m3AnEgSiUjKMLMLq1yNAUOpYSGuNLTCzFoRbIP0upltAlZFmigBmNn/VbkaAwajntikpMVxRERERKTOzGx0latlwBKCTe7XRZMo8YSLk7UExrp7SdR5omRmVVfhjb9fnnX3omgSyf5S4SgikmJ2Wbii2k0Ee2el9QIWIiINwcxuA94G3nX3gqjziNQ3FY4iIiIisldmdou732lmf6bmPWJviCBWwjCzq4ETgGMJpga8DUx29xcjDRYR7SmcejTHUUQkRWnvLBGpZ/PD85mRpkhQ7v4I8IiZHQRcAtwMXE+wMFk6eiw8vyvSFFJv1OMoIpKizGxulauVe2e5u/bOEhGpZ2b2ENAPWEvQ2zgF+MDdyyINJlJP1OMoIpKi3P2IqtfNbDDwjYjiiEiKMLOhwM+AHlT5LenuAyMLlRjaAhnAZmAjsEFFI5jZOcBv2Pl+0Xz7JKUeRxGRNGJmH7j74KhziEjyMrMFwA+BuUBFvN3dl0YWKoGY2eHAGcBNQIa7d404UqTMbBFwITDXVXgkNfU4ioikKO2dJSINZL27vxR1iEQT9qydCJwEtAYmEgxZTXfLgXkqGpOfehxFRFKU9s4SkYZgZqcCXwYmAMXxdnd/LrJQCcDM/gpMBt5291VR50kUZjaMYKjqW1R/v9wdWSjZL+pxFBFJUe7+66gziEhKugo4DMhi51BVB9K2cDSzDOBQd/9O1FkS0O+A7QSLtGVHnEUOgApHEZEUY2a1DiHT3lkicoAG7br4Vrpz93Iz22FmLd19S9R5Ekwbdx8ZdQg5cCocRURSz7EEc0r+C0wjWMFORKS+TDWzfu7+cdRBEkwRMNfMXgcK4o3ufkN0kRLCG2Y20t3HRx1EDozmOIqIpJhwyNTpBHOQBgKvAP91948iDSYiKcHM5gN9gMUEc9bi2yuk9XYcZnZlTe3uPqaxsyQSM9sGNAVKwpO240hSKhxFRFKYmeUQFJB/BG5z9z9HHElEkpyZ9aipXdtxiKQ2DVUVEUlBYcF4NkHR2BO4nzReuEJE6o+7LzWzE4C+7j7azNoDzaLOFRUze8rdLzGzuQSLBFWjnlgz4CtAL3f/jZl1Azq5+/SIo8k+Uo+jiEiKMbMxwADgNeAJd58XcSQRSSHhVj9DCVYRPcTMOgNPu/vxEUeLhJl1cvfV6omtmZk9QLD67gh3P9zMWgPj3X1YxNFkH6lwFBFJMWZWwc6FGap+yGteiYgcMDObBRwFfODuR4Vtc9K9Z21XZnY8cHm6b9FhZh+4+2Az+7DK+2W2uw+KOpvsGw1VFRFJMe4eizqDiKS0End3M3MAM2sadaBEYWZHApcDlxAsHqQpAlAaLtoWf7+0Z+f+n5JEVDiKiIiIyL54ysz+AbQys+uAq4EHI84UGTM7BLiMYE55PvAkwai+UyINljjuB54HOpjZ74CLgJ9HG0n2h4aqioiIiEidhAuddAUOA0YSDIEf5+6vRxosQuH0gLeBa9x9Udj2ubv3jjZZ9MwsBgwHNgKnErxfJrj7/EiDyX5R4SgiIiIidWZm77v7kKhzJAozu4Cgx/E4YCzwBPCQu/eKNFiCMLP33P3YqHPIgdM8GBERERHZF1PNTCtihtz9eXe/lKAX9k3gJqCjmT1gZiMjDZcYxpvZl8Leakli6nEUERERkTozs4+BQ4ElBCs4x1ds1qqqITNrA1wMXOruI6LOEyUz2wY0BcqAIrTCd9JS4SgiIiIidab9CkXSk1ZVFREREZG9MrMOwE+Bg4G5wO3uvjXaVJKozKwvcBfQB5gD/NDdV0abSg6E5jiKiIiISF08SjA09c9AM4JtFkT25BHgZeBLwIcE7xtJYhqqKiIiIiJ7ZWaz3P3IKtc/cPfBEUZKKGZ2h7v/aG9t6ULvl9SjHkcRERERqQszs9Zm1iZc/CVjl+vp7vQa2s5s9BSJI9fMjjKzwWY2GMjb5bokGfU4ioiIiMhemdkSoIJgVcxdebpueG9m3wK+DfQGPqtyU3PgHXe/IpJgETOzSbXc7Om+2mwyUuEoIiIiIrKfzKwl0Bq4HfhxlZu2ufvGaFKJ1D8VjiIiIiIi9cDMTgD6uvtoM2sHNHf3xVHnEqkPKhxFRERERA6Qmd0KDAUOdfdDzKwz8LS7Hx9xNJF6ocVxREREREQO3AXAuQRbluDuqwjmOYqkBBWOIiIiIrLPzKyDmXWPn6LOkwBKPBjK5wBm1jTiPAnBzI6PvxZmdoWZ3W1mPaLOJftOhaOIiIiI1JmZnWtmC4HFwFvAEuC1SEMlhqfM7B9AKzO7DpgAPBRxpkTwALDDzAYBtwBLgUejjST7Q3McRURERKTOzGw2MAJ4w92PMrNTgC+7+/URR4ucmZ0OjAyvjnP3N6LMkwjM7AN3H2xmvwRWuvvD8baos8m+yYw6gIiIiIgklVJ3zzezmJnF3H2Smd0RdaiomNk2wuGpVN/j8ptmVkSwt+PP3H1Co4dLDNvM7CfAFcBJZpYBZEWcSfaDCkcRERER2RebzawZMBn4j5mtA8oizhQZd9/jAjhhkTQA+E94no4uBS4HrnH3NeF82D9GnEn2g4aqioiIiEidhQudFBKslfEVoCXwH3fPjzRYAjOzb7j7P6LO0djCwnmcu58WdRY5cCocRURERKROVAjIvjKzl4CvuvuWqLPIgdFQVRERERGpE3cvN7MdZtZShYDUUREw18xeJ9zjEsDdb4gukuwPFY4iIiIisi9UCMi+eCU8SZLTUFURERERqTMzu7Kmdncf09hZJDmYWR7Q3d0XRJ1F9p8KRxERERERaRBm9kXgLiDb3XuZ2ZHAbe5+brTJZF/Fog4gIiIiIsnDzPqa2TNm9rGZfR4/RZ1LEtavgKOBzQDuPgvoFV0c2V8qHEVERERkX4wGHiDYu/EU4FHgsUgTSSIrq2EhJQ15TEIqHEVERERkX+S5+wSCKU9L3f1XwIiIM0nimmdmlwMZYW/1n4F3ow4l+06Fo4iIiIjsiyIziwELzey7ZnYB0CHqUJKwvgf0B4qB/wJbge9HGUj2jxbHEREREZE6M7NhwHygFfAboAVwp7tPizKXiDQs7eMoIiIiIvuip7vPALYDVwGY2cWACkepZGb3uvv3zex/1DCnUauqJh/1OIqIiIhInZnZB+4+eG9tkt7MbIi7v29mX6jpdnd/q7EzyYFRj6OIiIiI7JWZnQmcBXQxs/ur3NSCYIVVkUph0ZgBXOfuV0SdRw6cCkcRERERqYtVwEzgXOD9Ku3bgJsiSSQJzd3Lzay9mWW7e0nUeeTAaKiqiIiIiNSZmWW5e2l4uTXQzd3nRBxLEpSZ/QMYDLwEFMTb3f3uyELJflGPo4iIiIjsi9fN7FyC35GzgPVm9pa7/1+0sSRBrQpPMaB5xFnkAKhwFBEREZF90dLdt5rZtcBod7/VzNTjKLsJ5zj21RzH1BCLOoCIiIiIJJVMM+sEXAK8HHUYSVzuXg60N7PsqLPIgVOPo4iIiIjsi9uAccAUd59hZr2BhRFnksS1BHjHzDTHMclpcRwREREREWkQZnZrTe3u/uvGziIHRoWjiIiIiOyVmd3i7nea2Z+B3X5AuvsNEcQSkUaioaoiIiIiUhcfh+czI00hScXM2gO3AP2B3Hi7u4+ILJTsFxWOIiIiIlIXo8xso7uPiTqIJJX/AE8C5wDfBK4E1keaSPaLVlUVERERkbpYCPzJzJaY2R1mdmTUgSQptHX3h4FSd3/L3a8GhkcdSvadCkcRERER2St3v8/djwW+AGwERpvZfDP7pZkdEnE8SVyl4flqMzvbzI4CukYZSPaPFscRERERkf0SFgGPAAPdPSPqPJJ4zOwc4G2gG/BnoAXwa3d/KdJgss9UOIqIiIhInZlZFjAKuAw4FXgL+K+7vxBlLhFpWBqqKiIiIiJ7ZWanm9kjwArgeuBVoI+7X6qiUfbEzMaYWasq11uH7yNJMupxFBEREZG9MrNJwOPAs+6+Meo8khzM7EN3P2pvbZL4tB2HiIiIiOyVu58SdQZJSjEza+3umwDMrA2qQZKS/qeJiIiIiEhD+RPwrpk9AzhwCfC7aCPJ/tBQVRERERERaTBm1g8YARgwwd0/jjiS7AcVjiIiIiIiIlIrraoqIiIiIiIitVLhKCIiIiIiIrVS4SgiIiIiIg3GzHqY2Wnh5Twzax51Jtl3KhxFRERERKRBmNl1wDPAP8KmrsALkQWS/abCUUREREREGsp3gOOBrQDuvhDoEGki2S8qHEVEREREpKEUu3tJ/IqZZRLs5yhJRoWjiIiIiIg0lLfM7KdAnpmdDjwN/C/iTLIftI+jiIiIiIg0CDOLAdcAIwEDxgEPuYqQpKPCUURERERERGqVGXUAERERERFJLWY2l1rmMrr7wEaMI/VAPY4iIiIiIlKvzKxHbbe7+9LGyiL1Q4WjiIiIiIg0GDM7CDiaoAdyhruviTiS7AetqioiIiIiIg3CzK4FpgMXAhcBU83s6mhTyf5Qj6OIiIiIiDQIM1sAHOfu+eH1tsC77n5otMlkX6nHUUREREREGsoKYFuV69uA5RFlkQOgHkcREREREWkQZvYocATwIsEcx/MIhq5+CuDud0eXTvaFtuMQEREREZGG8ll4insxPG8eQRY5AOpxFBERERERkVqpx1FEREREROqVmd3r7t83s/8RDFGtxt3PjSCWHAAVjiIiIiIiUt8eC8/vijSF1BsVjiIiIiIiUq/c/f3w4pHufl/V28zsRuCtxk8lB0LbcYiIiIiISEO5soa2rzd2CDlw6nEUEREREZF6ZWZfBi4HepnZS1Vuag7kR5NKDoQKRxERERERqW/vAquBdsCfqrRvA+ZEkkgOiLbjEBERERERkVqpx1FEREREROqVmW2jhm04AAPc3Vs0ciQ5QOpxFBERERERkVqpx1FERERERBqEmXWvqd3dlzV2Fjkw6nEUEREREZEGYWZzq1zNBXoBC9y9f0SRZD+px1FERERERBqEux9R9bqZDQa+EVEcOQCxqAOIiIiIiEh6cPcPgGFR55B9px5HERERERFpEGb2f1WuxoDBwPqI4sgBUOEoIiIiIiINpXmVy2XAK8CzEWWRA6DFcURERERERKRW6nEUEREREZF6ZWYv1Xa7u5/bWFmkfqhwFBERERGR+nYssBz4LzANsGjjyIHSUFUREREREalXZpYBnA58GRhIMLfxv+7+UaTBZL9pOw4REREREalX7l7u7mPd/UpgOLAIeNPMvhdxNNlPGqoqIiIiIiL1zsxygLMJeh17AvcDz0WZSfafhqqKiIiIiEi9MrMxwADgNeAJd58XcSQ5QCocRURERESkXplZBVAQXq1acBjg7t6i8VPJgVDhKCIiIiIiIrXS4jgiIiIiIiJSKxWOIiIiIiIiUisVjiIiIiIiIlIrFY4iIiL1zMwuMDM3s8PC653N7Jk93Lenmc0LLw81s/sbM6uIiEhdaHEcERGRemZmTwGdgAnu/qta7pcJdAVedvcBjRRPRERkn6nHUUREpB6ZWTPgeOAa4LKwrWqv4tfN7Gkz+x8wfpfHnmxmL4eXf2Vmj5jZm2b2uZndUOV+V5jZdDObZWb/MLOMxnp+IiKSnlQ4ioiI1K/zgbHu/imw0cwG13CfY4Er3X3EXv7WYcAZwNHArWaWZWaHA5cCx7v7kUA58JX6Ci8iIlITFY4i/9/eHaNEFkRRAL0PXYGCRqIYm80OdAuduBTFdZhrZDJMZKK4gkkGA9PJBzEzMJBn0B1IC0WDfxDknKjq83n1suJSUAUwreMkV4vx1WK+7La7n1aodd3dL939mORfku0kR0l+JPldVX8W8/1Pdw0AA+tf3QAAfBdVtZnkMMlBVXWStSSd5Hzp1+cVS768G79mvm9XkovuPvlkuwCwMieOADCdWZLL7t7t7r3u3knyN/MLcKZyl2RWVVtJUlUbVbU7YX0A+EBwBIDpHCf5tfTtZ5LTqRbo7ockZ0luquo+yW3mN7gCwH/jOQ4AAACGnDgCAAAwJDgCAAAwJDgCAAAwJDgCAAAwJDgCAAAwJDgCAAAwJDgCAAAw9AY8mN/CZ3O4CAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "sns.violinplot(x='Airline',y='Price',data=data)\n",
    "plt.xticks(rotation='vertical')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d4442758",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No info                         78.112713\n",
       "In-flight meal not included     18.554578\n",
       "No check-in baggage included     2.995694\n",
       "1 Long layover                   0.177869\n",
       "Change airports                  0.065531\n",
       "Business class                   0.037446\n",
       "No Info                          0.028085\n",
       "1 Short layover                  0.009362\n",
       "Red-eye flight                   0.009362\n",
       "2 Long layover                   0.009362\n",
       "Name: Additional_Info, dtype: float64"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Additional_Info'].value_counts()/len(data)*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e574b29e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No info                         78.11\n",
       "In-flight meal not included     18.55\n",
       "No check-in baggage included     3.00\n",
       "1 Long layover                   0.18\n",
       "Change airports                  0.07\n",
       "Business class                   0.04\n",
       "No Info                          0.03\n",
       "1 Short layover                  0.01\n",
       "Red-eye flight                   0.01\n",
       "2 Long layover                   0.01\n",
       "Name: Additional_Info, dtype: float64"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.round(data['Additional_Info'].value_counts()/len(data)*100,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "c78446fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>Duration_total_min</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>445</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>DEL → LKO → BOM → COK</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>1140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>CCU → NAG → BLR</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>325</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → NAG → DEL</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>285</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination                  Route Duration  \\\n",
       "0       IndiGo  Banglore   New Delhi              BLR → DEL   2h 50m   \n",
       "1    Air India   Kolkata    Banglore  CCU → IXR → BBI → BLR   7h 25m   \n",
       "2  Jet Airways     Delhi      Cochin  DEL → LKO → BOM → COK   19h 0m   \n",
       "3       IndiGo   Kolkata    Banglore        CCU → NAG → BLR   5h 25m   \n",
       "4       IndiGo  Banglore   New Delhi        BLR → NAG → DEL   4h 45m   \n",
       "\n",
       "  Total_Stops Additional_Info  Price  Joruney_day  Joruney_month  \\\n",
       "0    non-stop         No info   3897           24              3   \n",
       "1     2 stops         No info   7662            5              1   \n",
       "2     2 stops         No info  13882            6              9   \n",
       "3      1 stop         No info   6218            5             12   \n",
       "4      1 stop         No info  13302            3              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \\\n",
       "0             22               20                  1                   10   \n",
       "1              5               50                 13                   15   \n",
       "2              9               25                  4                   25   \n",
       "3             18                5                 23                   30   \n",
       "4             16               50                 21                   35   \n",
       "\n",
       "   Duration_total_min  \n",
       "0                 170  \n",
       "1                 445  \n",
       "2                1140  \n",
       "3                 325  \n",
       "4                 285  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b863022",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "a214f30a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.drop(columns=['Additional_Info','Route','Duration_total_min'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "7c11e691",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination Duration Total_Stops  Price  Joruney_day  \\\n",
       "0       IndiGo  Banglore   New Delhi   2h 50m    non-stop   3897           24   \n",
       "1    Air India   Kolkata    Banglore   7h 25m     2 stops   7662            5   \n",
       "2  Jet Airways     Delhi      Cochin   19h 0m     2 stops  13882            6   \n",
       "3       IndiGo   Kolkata    Banglore   5h 25m      1 stop   6218            5   \n",
       "4       IndiGo  Banglore   New Delhi   4h 45m      1 stop  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  \n",
       "0                   10  \n",
       "1                   15  \n",
       "2                   25  \n",
       "3                   30  \n",
       "4                   35  "
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "171eeb35",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5e5ae472",
   "metadata": {},
   "outputs": [],
   "source": [
    "cat_col=[col for col in data.columns if data[col].dtypes=='object']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "977cc24f",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_col=[col for col in data.columns if data[col].dtypes!='object']"
   ]
  },
  {
   "cell_type": "raw",
   "id": "f797922b",
   "metadata": {},
   "source": [
    "cat_col"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "48f3f17d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Airline', 'Source', 'Destination', 'Duration', 'Total_Stops']"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_col"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "2cd9103b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'], dtype=object)"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Source'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "67231ff1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        Banglore\n",
       "1         Kolkata\n",
       "2           Delhi\n",
       "3         Kolkata\n",
       "4        Banglore\n",
       "           ...   \n",
       "10678     Kolkata\n",
       "10679     Kolkata\n",
       "10680    Banglore\n",
       "10681    Banglore\n",
       "10682       Delhi\n",
       "Name: Source, Length: 10682, dtype: object"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Source']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "42bdcfe1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        1\n",
       "1        0\n",
       "2        0\n",
       "3        0\n",
       "4        1\n",
       "        ..\n",
       "10678    0\n",
       "10679    0\n",
       "10680    1\n",
       "10681    1\n",
       "10682    0\n",
       "Name: Source, Length: 10682, dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Source'].apply(lambda x: 1 if x=='Banglore' else 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "1c120d3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "for category in data['Source'].unique():\n",
    "    data['Source'+category]=data['Source'].apply(lambda x: 1 if x==category else 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "531adc0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Air India</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Jet Airways</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Airline    Source Destination Duration Total_Stops  Price  Joruney_day  \\\n",
       "0       IndiGo  Banglore   New Delhi   2h 50m    non-stop   3897           24   \n",
       "1    Air India   Kolkata    Banglore   7h 25m     2 stops   7662            5   \n",
       "2  Jet Airways     Delhi      Cochin   19h 0m     2 stops  13882            6   \n",
       "3       IndiGo   Kolkata    Banglore   5h 25m      1 stop   6218            5   \n",
       "4       IndiGo  Banglore   New Delhi   4h 45m      1 stop  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()\n",
    "#one hot or not \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "bd566555",
   "metadata": {},
   "outputs": [],
   "source": [
    "airlines=data.groupby(['Airline'])['Price'].mean().sort_values().index\n",
    "#encoading of the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "7a037784",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Trujet', 'SpiceJet', 'Air Asia', 'IndiGo', 'GoAir', 'Vistara',\n",
       "       'Vistara Premium economy', 'Air India', 'Multiple carriers',\n",
       "       'Multiple carriers Premium economy', 'Jet Airways',\n",
       "       'Jet Airways Business'],\n",
       "      dtype='object', name='Airline')"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "airlines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "80d4d943",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1={key:index for index,key in enumerate(airlines,0)}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e0af68f",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "9fc2908c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Airline']=data['Airline'].map(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "23cd8a5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         3\n",
       "1         7\n",
       "2        10\n",
       "3         3\n",
       "4         3\n",
       "         ..\n",
       "10678     2\n",
       "10679     7\n",
       "10680    10\n",
       "10681     5\n",
       "10682     7\n",
       "Name: Airline, Length: 10682, dtype: int64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Airline']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "479dfa48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline    Source Destination Duration Total_Stops  Price  Joruney_day  \\\n",
       "0        3  Banglore   New Delhi   2h 50m    non-stop   3897           24   \n",
       "1        7   Kolkata    Banglore   7h 25m     2 stops   7662            5   \n",
       "2       10     Delhi      Cochin   19h 0m     2 stops  13882            6   \n",
       "3        3   Kolkata    Banglore   5h 25m      1 stop   6218            5   \n",
       "4        3  Banglore   New Delhi   4h 45m      1 stop  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "bd7990e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Destination'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "961e0d74",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Destination'].replace('New Delhi','Delhi',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "af8ae39a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Destination'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "67db1c65",
   "metadata": {},
   "outputs": [],
   "source": [
    "dest=data.groupby(['Destination'])['Price'].mean().sort_values().index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "8df1e68f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Kolkata', 'Hyderabad', 'Delhi', 'Banglore', 'Cochin'], dtype='object', name='Destination')"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "37108e6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict2={key:index for index,key in enumerate(dest,0)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "c0fe0615",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Kolkata': 0, 'Hyderabad': 1, 'Delhi': 2, 'Banglore': 3, 'Cochin': 4}"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "7a7957fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Cochin</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline    Source Destination Duration Total_Stops  Price  Joruney_day  \\\n",
       "0        3  Banglore       Delhi   2h 50m    non-stop   3897           24   \n",
       "1        7   Kolkata    Banglore   7h 25m     2 stops   7662            5   \n",
       "2       10     Delhi      Cochin   19h 0m     2 stops  13882            6   \n",
       "3        3   Kolkata    Banglore   5h 25m      1 stop   6218            5   \n",
       "4        3  Banglore       Delhi   4h 45m      1 stop  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "d61c5263",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Destination']=data['Destination'].map(dict2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "7f8f50f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>4</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline    Source  Destination Duration Total_Stops  Price  Joruney_day  \\\n",
       "0        3  Banglore            2   2h 50m    non-stop   3897           24   \n",
       "1        7   Kolkata            3   7h 25m     2 stops   7662            5   \n",
       "2       10     Delhi            4   19h 0m     2 stops  13882            6   \n",
       "3        3   Kolkata            3   5h 25m      1 stop   6218            5   \n",
       "4        3  Banglore            2   4h 45m      1 stop  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "b4c3b8cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>4</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1 stop</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline    Source  Destination Duration Total_Stops  Price  Joruney_day  \\\n",
       "0        3  Banglore            2   2h 50m    non-stop   3897           24   \n",
       "1        7   Kolkata            3   7h 25m     2 stops   7662            5   \n",
       "2       10     Delhi            4   19h 0m     2 stops  13882            6   \n",
       "3        3   Kolkata            3   5h 25m      1 stop   6218            5   \n",
       "4        3  Banglore            2   4h 45m      1 stop  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "bffada05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['non-stop', '2 stops', '1 stop', '3 stops', '4 stops'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Total_Stops'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "15bf8c4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "stops={'non-stop':0,'2 stops':2,'1 stop':1,'3 stops':3,'4 stops':4}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "0661371e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'non-stop': 0, '2 stops': 2, '1 stop': 1, '3 stops': 3, '4 stops': 4}"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "302f40de",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Total_Stops']=data['Total_Stops'].map(stops)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "b6a6ed46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>0</td>\n",
       "      <td>3897</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2</td>\n",
       "      <td>7662</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>4</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2</td>\n",
       "      <td>13882</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1</td>\n",
       "      <td>6218</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1</td>\n",
       "      <td>13302</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline    Source  Destination Duration  Total_Stops  Price  Joruney_day  \\\n",
       "0        3  Banglore            2   2h 50m            0   3897           24   \n",
       "1        7   Kolkata            3   7h 25m            2   7662            5   \n",
       "2       10     Delhi            4   19h 0m            2  13882            6   \n",
       "3        3   Kolkata            3   5h 25m            1   6218            5   \n",
       "4        3  Banglore            2   4h 45m            1  13302            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "a6c4beb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot(df,col):\n",
    "    fig,(ax1,ax2,ax3)=plt.subplots(3,1)\n",
    "    sns.distplot(df[col],ax=ax1)\n",
    "    sns.boxplot(df[col],ax=ax2)\n",
    "    sns.distplot(df[col],ax=ax3,kde=False)\n",
    "    \n",
    "    #data outliers \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "33108739",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Shreyas\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2557: FutureWarning:\n",
      "\n",
      "`distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "C:\\Users\\Shreyas\\anaconda3\\lib\\site-packages\\seaborn\\_decorators.py:36: FutureWarning:\n",
      "\n",
      "Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "\n",
      "C:\\Users\\Shreyas\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2557: FutureWarning:\n",
      "\n",
      "`distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZ4AAAEGCAYAAABVSfMhAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAApJklEQVR4nO3de3RdVbn38e+TpEl6b5OU0ntaWoQCCiXSgpdTsIWW46GOoZ5ThENVhFdBQHnPq+XIURgvjKEOX1+F4wErB21VbopHCm9baDkoiEBJEeidBnqh9zTQ+y2X5/1jzYTdXHfS7LVXkt9njD322nPNufazZ9o8WXPNPZe5OyIiInHJyXYAIiLSsyjxiIhIrJR4REQkVko8IiISKyUeERGJVV62A0iqkpISLy0tzXYYIiJdyooVK/a4+5DW6ijxtKC0tJTy8vJshyEi0qWY2ea26mioTUREYqUzngR56JUtTcq+MHl0FiIREckcnfGIiEislHhERCRWSjwiIhIrJR4REYlVRhOPmc0ws/VmVmFmc5vZb2Z2T9j/pplNaqutmRWZ2VIz2xCeB4fyYjN7zswOmtm/N3qf881sZTjWPWZmmfzcneHA0Wre2LoXrR4uIt1NxhKPmeUCPwNmAhOBK81sYqNqM4EJ4XE9cF8abecCz7r7BODZ8BrgKPBvwL80E8594fj17zWjEz5iRj3+2lYeffVd7nxyjZKPiHQrmTzjuQCocPd33P048Agwq1GdWcACj7wMDDKzYW20nQXMD9vzgc8AuPshd/8LUQJqEI43wN1f8ug3+IL6Nkn1duVB3tp1kFMHFPKrv27igRc2ZjskEZFOk8nEMwJ4N+X11lCWTp3W2g519x0A4fmUNOLY2kYcAJjZ9WZWbmbllZWVbRw2M9ydJat2MrB3L7429TQ+MaGEeS+8w/GauqzEIyLS2TKZeJq7jtJ4zKilOum07cw4okL3ee5e5u5lQ4a0utRQxuw/WsO2vUf42GnF9MrN4SufGEflgWP8v5XbsxKPiEhny2Ti2QqMSnk9Emj827OlOq213RWGz+qH0XanEcfINuJIjO17jwAwqqgPAJ+cUMJpQ/ry4F826VqPiHQLmUw8rwITzGysmeUDs4GFjeosBK4Js9umAPvC8FlrbRcCc8L2HOCJ1oIIxztgZlPCbLZr2mqTTdv3HsGAYQN7A2BmfPnjY1m5bR9/fis7w38iIp0pY4nH3WuArwNPA2uBx9x9tZl91cy+GqotAt4BKoBfADe01ja0+T4w3cw2ANPDawDMbBPwY+CLZrY1ZSbc14AHwvu8DSzOyIfuBNv3HqGkfwH5eR/8aD5//ihGFfXmB0vWU1ensx4R6drSWiTUzB4HHgQWu3vaV7ndfRFRckktuz9l24Eb020byquAT7XQprSF8nLg7HTjzqZte48wbki/E8ry83L4n9M/xDcefZ3fLt/CP08Zk6XoREROXrqrU98HfAm4x8x+B/zK3ddlLqye6cDRavYfrWH4wMIm+674yHB++8pm/u2Pq/jvtbso7JVL7/xczho+kH+eMuaEMyQRkSRLK/G4+zJgmZkNBK4ElprZu0TDY79x9+oMxthj7NgXfQVp+KDeTfbl5Bi//coU/v25Ch5ZvgV3OFZTyx9e28YTr2/jH8tGkWOm2yiISOKlfT8eMysGrgb+Gfgb8Fvg40QX+KdmIriepn5GW3OJB6Iht1unn86t009vuHfP829VsmT1Tgb3yeeys06NLVYRkY5K9xrPH4AzgF8D/1D/BU7gUTPT/aE7SeWBYwzs3YvCXrlpt/nEhBJ27T/KXyr2MHlsUQajExHpHOme8TwQLvY3MLMCdz/m7mUZiKtHqjp0nOK++SeUNXdX0lRmxrSJQ3lj617+/FYlN1w8vtl6LR1HQ3MiErd0r0jf1UzZS50ZiESJp6hR4knH4D75nD+miPLN77Nj35EMRCYi0nlaTTxmdqqZnQ/0NrPzzGxSeEwF+sQRYE9x4Gg1h47VUNyvoEPt/+70IdTVOb95eXMnRyYi0rnaGmq7DPgi0TIzP04pPwD8a4Zi6pE2Vx0GaDLUlq6ivvmccWp/Hln+Ljd/agIFeelfJxIRiVOrZzzuPt/dLwa+6O4XpzyucPc/xBRjj9CQePp1LPEATDmtmKpDx1m0ckez+6tr61j4xjZe2FDJ/iOaAS8i2dHqGY+ZXe3uvwFKzezWxvvd/cfNNJMO2FR1CKBD13jqnTakH+NK+vLLFzfxmXNH0PhGq4tX7eDld94D4M9vVXLr9NM7HrCISAe1NdTWNzz3a7WWnLTNVYfoX5B3UkNkOWZc+4mxfOe/VvFiRRUfn1DSsG/19n28/M57fHx8CWcPH8D9z7/DXyr28JVPjGtyHM2AE5FMajXxuPvPw/Od8YTTc22qOkzRSQyz1fvc+SO559kN/Oy5iobEc+BoNQvf2M7wQYVcetZQ8nJyOGfEQP76dhXvHzrO4GbOst4/dJx1O/czcnAfRgzuTY41d1sjEZH2S2s6tZn90MwGmFkvM3vWzPaY2dWZDq4n2VJ1mOK+HZvRlqogL5frPjGOl96pYtmaXQD8dNkGDh6t4TPnjiAvJ/qRX3LGKVTX1DHvhXeaHOMvFXv4v8ve4sk3d3Dfn9/mF8+/w+FjNScdm4gIpP89nkvdfT/waaIbq50O/K+MRdXDHDley879R0/q+k6qqyaP4azhA7jxode4+eG/8eCLGykrLWLk4A9mwA8dUMiHRw5k/l83UXXwWEP5E69vY9HKHYw/pR83XzKBKz4ynG17j3D/82+fUE9EpKPSTTy9wvPlwMPu/l6G4umRtrx38jPaUvXOz+XX105mdFEfFq/awdVTxnD52U3XcbvkjKEcra5l3vPRWc8b7+7l24+/SWlxX66aPIZTBxYyZVwxX/rYWN4/XM2//tdK3QVVRE5aukvmPGlm64AjwA1mNgQ4mrmwepb6GW0d/Q5PqtSJAV+YPJrqWqdfQfM/5iH9C/jMuSN48MWN7D9azcLXt1Pct4ArLxhFbs4H13TGlvRl+plDWbJ6J4+/to3PnT+y2eOJiKQjrTMed58LXAiUhVsgHAJmZTKwnmRzQ+I5+Ws8qQrycltMOvW++w8TmXXuCB5e/i6jivrwhxsuon9hryb1Pj6hhEmjB/HjZ9ZTU5v2vQBFRJpoz93DzgT+ycyuAT4HXNpWAzObYWbrzazCzOY2s9/M7J6w/00zm9RWWzMrMrOlZrYhPA9O2XdbqL/ezC5LKf9TKHs9PE5px+fOuE1Vhxncpxe98+NfbWBQn3x+9PmP8Kd/mcofbriIoQOa3oQOoqna13/yNLbvO8qz63bHHKWIdCfpzmr7NfAjovvvfDQ8Wl2V2sxygZ8BM4GJwJVmNrFRtZnAhPC4nuhOp221nQs86+4TgGfDa8L+2cBZwAzgP8Jx6l3l7ueGR6J+c26uOsSY4r5tV8yg0pK+9Mlv/exo2pmnMHxgIb9+SevBiUjHpXuNpwyY6O27snwBUOHu7wCY2SNEw3NrUurMAhaE475sZoPMbBhQ2krbWXxw47n5wJ+Ab4fyR9z9GLDRzCpCDIlfRXtz1WHKxgxuu2KW5eXm8IXJo/nRM2/xTuVBxg3R94pFpP3SHWpbBbT39pYjgHdTXm8NZenUaa3t0Pob0YXn+mGztt7vl2GY7d+s8VoyWXSsppbte48wOstnPOn6bJhY8Ez4jpCISHule8ZTAqwxs+VAw5c53P2KVto098u98RlTS3XSadue97vK3beZWX/gcaLbdy9ocgCz64mG/Bg9Op7lYba+f4Q6h9LiPhytTvZF+/oZc8MGFvLI8ncZECYhaCkdEWmPdBPPHR049lZgVMrrkcD2NOvkt9J2l5kNc/cdYViu/npNi+/n7tvC8wEze4hoCK5J4nH3ecA8gLKysli+sFI/o21McV/W7zwQx1ueoK07nDbnQ0P78/yGSo4cr83KhAgR6drSnU79Z2AT0Ctsvwq81kazV4EJZjbWzPKJLvwvbFRnIXBNmN02BdgXhs9aa7sQmBO25wBPpJTPNrMCMxtLNGFhuZnlmVkJgJn1Ilp9YVU6nzsOm/ZEXx4tLe4699X70Kn9qXPYsDv+RCkiXV9aZzxmdh3REFQRcBrRtZP7gU+11Mbda8zs68DTQC7woLuvNrOvhv33A4uIVkOoAA4DX2qtbTj094HHzOxaYAvw+dBmtZk9RjQBoQa40d1rzawv8HRIOrnAMuAX6XzuOGwKq1J31nI5cRhV1IfevXJZv/MAHx45KNvhiEgXk+5Q241Ew1OvALj7hnS+C+Pui4iSS2rZ/SnbHo6dVttQXkULCc/d7wbublR2CDi/rVizZd3OA5x+av8m985JshwzJgztx4bdB7WEjoi0W7qz2o65+/H6F2aWR9sX+6UN7s7a7fuZOGxAtkNptwmn9OPgsRp27tfKSSLSPukmnj+b2b8Cvc1sOvA74MnMhdUzbH3/CAeO1XBmF0w840/pD0DF7oNZjkREupp0E89coBJYCfwPoiGw2zMVVE+xevt+ACYO73qJZ2DvXgzpV6DEIyLtltY1HnevM7M/An9098rMhtRzrNmxnxyLpid3ReNP6Uf55vc4Wl1LYS9NqxaR9LR6xhOmOd9hZnuAdcB6M6s0s+/GE173tmb7fsYN6ddlvwsz/pR+VNc65Zvez3YoItKFtDXU9g3gY8BH3b3Y3YuAycDHzOybmQ6uu1u7o2tOLKh32pB+9Mo1lqzeke1QRKQLaSvxXANc6e4b6wvCwp1Xh33SQXsPH2fb3iNd8vpOvfy8HM44dQBLVu3UPXpEJG1tJZ5e7r6ncWG4ztP0bmGStpfergJg0ujkr0rdmnNGDGTPweMs36i7oYtIetpKPMc7uE/a8Kf1lfQvzGPS6EHZDuWknD60P33yc3lqpYbbRCQ9bc1q+4iZ7W+m3IDmb1Upbfrty5tZvGoHY4r68Fj51myHc1Ly83KYPnEoT76+nW9d9iEG9ek6S/+ISHa0esbj7rnuPqCZR39311BbB+3af4z9R2s4vYtOo27sq393GgeP1/CLF97Jdigi0gWk+wVS6URv7YpWdZ7QTRLPmcMG8OkPD+eXL26i8sCxthuISI+mxBMzd+fNbXsZNrCQgb27x0njQ69sYfyQfhyrruOqB17mNy9v7tB9fkSkZ1Diidnr7+5l+96jfLS0KNuhdKoh/Qv49EeG8daugyxbq9tii0jLlHhi9uuXN5Ofl8N5owZlO5ROd0FpEWVjBvOn9ZX8paLJLHwREUCJJ1Z7Dh7jqTd3cN6oQRR0w7XNzIxZ547grOEDWLRyB794XpMNRKQpJZ4Y/Z9n3qKuzrnotJJsh5IxuTnGP310FGePGMjdi9Zyx8LVHK2uzXZYIpIg6d6BVE7Sqm37eOTVLXzporEM6V+Q7XAyKi8nh9kfHcU7pUU8+OJG/vxWJTddMp7LzjqVvgX6JyfS02X0jMfMZpjZejOrMLO5zew3M7sn7H/TzCa11dbMisxsqZltCM+DU/bdFuqvN7PLUsrPN7OVYd89FvN9pt8/dJxbH3udoj753DJtQpxvnTU5Znz3Hybym2snY8Ctj73Bef97Kf/485f48TPrebFiD0eO60xIpCcy98zcwdrMcoG3gOnAVuBVogVH16TUuRy4CbicaNXrn7r75NbamtkPgffc/fshIQ1292+b2UTgYeACYDiwDDjd3WvNbDlwC/Ay0U3s7nH3xa3FX1ZW5uXl5SfdD5v2HOLmR/7Gup0H+NUXP8pF40t63FTjOnc2Vx1m7Y797DtSzert+6hz6JVrfHjkIMrGDGbE4N70L8wjNyeHXjlGbo7RKzeHvNxouyAvh+K+BZwyoIA++S2fNbk7+4/WsOfgMfYcOEblwWNUHTxObZ3TryCPUwYUMHxQb4YNLKR/YfeYzi6SJGa2wt3LWquTyXGPC4CKsJo1ZvYIMAtYk1JnFrDAo+z3spkNMrNhQGkrbWcBU0P7+cCfgG+H8kfc/Riw0cwqgAvMbBMwwN1fCsdaAHwGaDXxdNTvyt9l1/6j7DtSzfpdB3mxYg95OcZ9V03iovHd99pOa3LMGFvSl7ElfQE4Wl3L5qrDbNxziI17DvLACxupbccfQP0L8uhfmEfv/Fz65OdRXVvHsZo6Dh+v4f3D1RyvSW+l7P4FeQwbVMipA3szfGAhA/v0IteMHDNycgwDauuc6to6jtfWUV1bR3VN9Dov1yjIy6UgL4eCXjnk50aTRZzoc9R/nIZPFQoaf0qz6H1yzDCL1qLKybGGfmsoC9v1bUQyac6FY8jLzdyAWCYTzwjg3ZTXW4nOatqqM6KNtkPdfQeAu+8ws1NSjvVyM8eqDtuNy5sws+uB68PLg2a2vqUPl4YSoGFO8bS7T+JI3d8JfRWnVdl4047LWj91Meqn9LTYT185ueOOaatCJhNPc3+WNfmDr4U66bRN9/3SPpa7zwPmtfE+aTGz8rZONyWivkqP+ik96qf0ZLOfMjm5YCswKuX1SGB7mnVaa7srDMcRnnencayRbcQhIiIxyWTieRWYYGZjzSwfmA0sbFRnIXBNmN02BdgXhtFaa7sQmBO25wBPpJTPNrMCMxsLTACWh+MdMLMpYTbbNSltREQkZhkbanP3GjP7OvA0kAs86O6rzeyrYf/9RDPMLgcqgMPAl1prGw79feAxM7sW2AJ8PrRZbWaPEU1AqAFudPf6+bpfA34F9CaaVJCRiQWNdMqQXQ+hvkqP+ik96qf0ZK2fMjadWkREpDlaMkdERGKlxCMiIrFS4smAtpYK6m7MbJSZPWdma81stZndEso7bXmjMGnk0VD+ipmVxv5BO4mZ5ZrZ38zsqfBa/dSM8IXy35vZuvBv60L1VVNm9s3w/26VmT1sZoWJ7yd316MTH0STId4GxgH5wBvAxGzHleHPPAyYFLb7Ey13NBH4ITA3lM8FfhC2J4Z+KQDGhv7KDfuWAxcSff9qMTAzlN8A3B+2ZwOPZvtzn0R/3Qo8BDwVXqufmu+n+cBXwnY+MEh91aSPRgAbgd7h9WPAF5PeT1nvuO72CD+4p1Ne3wbclu24Yu6DJ4jW2VsPDAtlw4D1zfUJ0ezFC0OddSnlVwI/T60TtvOIvnFt2f6sHeibkcCzwCUpiUf91LSfBoRfqNaoXH11Yn/Ur/JSFD7DU8ClSe8nDbV1vpaWAeoRwmn4ecArNFreCEhd3qilpZJaWt6ooY271wD7gOKMfIjM+gnwLSB1QTn1U1PjgErgl2FY8gEz64v66gTuvg34EdFXS3YQfRfyGRLeT0o8na8jy/10C2bWD3gc+Ia772+tajNlbS1v1OX71cw+Dex29xXpNmmmrNv3U5AHTALuc/fzgENEQ0Yt6ZF9Fa7dzCIaNhsO9DWzq1tr0kxZ7P2k7/G0oKSkxEtLS7MdhohIl7JixYo97j6ktTq6HWQLSktL6Yz78YiI9CRmtrmtOhpqExGRWCnxiIhIrJR4REQkVrrGkxD33nsvFRUVadfftm0bACNGdGym9vjx47nppps61FZE5GQo8SRERUUFr69aS22forTq5x7eB8DOY+3/EeYefq/dbUREOosST4LU9iniyBmXp1W397pFAGnXb66tiEg26BqPiIjESolHRERipcQjIiKxUuIREZFYKfGIiEislHhERCRWSjwiIhIrJR4REYmVEo+IiMRKiUdERGKlxNPJ7r33Xu69995sh9EtqC9Fuiet1dbJ2rPCtLROfSnSPemMR0REYqXEIyIisVLiERGRWCnxiIhIrJR4REQkVko8IiISKyUeERGJlRKPiIjESolHEu3w4cPMmDGDqVOncumll3LppZcyY8YMrrvuOioqKrj55pspLy9n6tSpTJ06lb//+7+noqKCiy++uKHN1KlTee6557jzzjuZOnUqs2bNoqqqquE9qqqquPnmm08oS1VVVcVnP/tZpk6dyoMPPthirFVVVXzta1/juuuu44YbbmiIr/64FRUVDfG19Z7ZkKmY6vvlhhtuaPPY5eXlXHLJJaxYsSK2OJP4s8iWuPpCiUcSbcuWLRw9ehSA48ePc/z4cY4ePcqGDRu46667WLlyJXfccUdD/UOHDnHXXXfh7g1tAO6++26ee+45APbt28eCBQsa2syfP5+VK1eeUJZq/vz5Df8RW6pTX2/t2rVs2LCBNWvWNMRX3+auu+5qiK+t98yGTMVU3y9r1qxp89h33HEHdXV1fO9734stziT+LLIlrr5Q4pHEOnz4MMeOHWtx/6ZNm3B3Dh482KS8sZqamhNeP/HEE1RVVVFVVcWSJUtwd5YsWdLkL72qqioWLlx4QllzZz1VVVUsXry42fiWLFlCeXl5Q1ybNm1i0aJFLb5nNrTVDydz3NR+Wbx4cYvHLi8vb/hZHjx4sNmzns6OM1OfuyuKsy+0Vlsn27ZtG0eOHOGWW25pV7uKigpyjnuGojpRztH9VFQcaHeMccv0Wm0LFizA3amrqwOgtraWBQsW8M1vfrOhzvz585tt9+Uvf/mEsvnz5zdJbvVqa2tPOCuDDxJhc++ZDfPnz2+1H07muKn9Ul1d3eKxG/fR9773PZ566qmMxpmpz90VxdkXOuNJYWbXm1m5mZVXVlZmO5wer364LFOWLl3KsmXLGn4x1tTUsHTp0hPqLFu2LK1jLVu2rMV4a2pqmpyVpe5r/J7Z0FY/nMxxU/vF3Vs8duM+aq7POjvOTH3urijOvtAZTwp3nwfMAygrK+vQb70RI0YA8NOf/rRd7W655RZWvLOrI2/ZbnWFAxg/bmi7Y4zbZZdd1upQ28maPn067s6iRYuoqakhLy+P6dOnn1Bn2rRpTYbamjNt2jSefPLJZpNPXl4ehYWFzf4ibe49s2HatGmt9sPJHDe1X8ysxWP369fvhD7q169fxuPM1OfuiuLsC53xSGKNHj06o8e/5pprmDNnDjk50X+D3NxcrrnmmhPqzJkzp9l2jc2ZM4e8vOb/jsvNzW0yjFRft7n3zIa2+uFkjpvaL7169Wrx2I376M4778x4nJn63F1RnH2hxCOJ1adPHwoKClrcX1paipk1+cu4tLS0Sd3GSWHWrFkUFxdTXFzMjBkzMDNmzJhBcXHxCfWKi4u54oorTihrfH2nvt7MmTObjW/GjBmUlZU1xFVaWsrll1/e4ntmQ1v9cDLHTe2XmTNntnjssrKyhp9lv379OP/88zMeZ6Y+d1cUZ18o8UiijR49msLCQgDy8/PJz8+nsLCQCRMmcPvtt3POOeec8Jdy3759uf322zGzhjYA3/nOd7j44osBGDhw4Al/zc2ZM4dzzjmnxb/w5syZ0/CfsLW/AufMmcOZZ57JhAkTmDhxYkN89W1uv/32hvjaes9syFRM9f0yceLENo99xx13kJOT0+zZTqbiTOLPIlvi6gvL9AXcrqqsrMzLy8vb3a5+plhHr/EcOePytOr3XrcIIO36jdue3wWu8XS0L0Uke8xshbuXtVZHZzwiIhIrJR4REYmVEo+IiMRKiUdERGKlxCMiIrFS4hERkVgp8YiISKy0VlsnGz9+fLZD6DbUlyLdkxJPJ7vpppuyHUK3ob4U6Z401CYiIrFS4hERkVgp8YiISKyUeEREJFZKPCIiEislHhERiZUSj4iIxEqJR0REYqXEIyIisVLiERGRWGnJnATJPfwevdctSrNuFUDa9Ru/DwxtdzsRkc6gxJMQ7V0Qc9u2GgBGjOhIAhmqBThFJGuUeBJCC2KKSE+hazwiIhIrJR4REYmVEo+IiMRKiUdERGJl7p7tGBLJzCqBza1UKQH2xBROeym2jklybJDs+BRbx3TH2Ma4+5DWKijxdJCZlbt7WbbjaI5i65gkxwbJjk+xdUxPjU1DbSIiEislHhERiZUST8fNy3YArVBsHZPk2CDZ8Sm2jumRsekaj4iIxEpnPCIiEislHhERiZUSTzuZ2QwzW29mFWY2N4Pv86CZ7TazVSllRWa21Mw2hOfBKftuCzGtN7PLUsrPN7OVYd89ZmahvMDMHg3lr5hZaTtiG2Vmz5nZWjNbbWa3JCU+Mys0s+Vm9kaI7c6kxJZy3Fwz+5uZPZXA2DaF475uZuVJis/MBpnZ781sXfi3d2ESYjOzD4X+qn/sN7NvJCG20Pab4f/CKjN72KL/I9mNzd31SPMB5AJvA+OAfOANYGKG3uuTwCRgVUrZD4G5YXsu8IOwPTHEUgCMDTHmhn3LgQsBAxYDM0P5DcD9YXs28Gg7YhsGTArb/YG3QgxZjy8cp1/Y7gW8AkxJQmwpMd4KPAQ8laSfa2izCShpVJaI+ID5wFfCdj4wKCmxNfodsRMYk4TYgBHARqB3eP0Y8MVsx5b1X+Zd6RE6/emU17cBt2Xw/Uo5MfGsB4aF7WHA+ubiAJ4OsQ4D1qWUXwn8PLVO2M4j+oaydTDOJ4DpSYsP6AO8BkxOSmzASOBZ4BI+SDyJiC202UTTxJP1+IABRL9ALWmxNYrnUuDFpMRGlHjeBYpCu6dCjFmNTUNt7VP/Q6y3NZTFZai77wAIz6e0EdeIsN24/IQ27l4D7AOK2xtQOK0+j+jMIhHxhaGs14HdwFJ3T0xswE+AbwF1KWVJiQ3AgWfMbIWZXZ+g+MYBlcAvwzDlA2bWNyGxpZoNPBy2sx6bu28DfgRsAXYA+9z9mWzHpsTTPtZMWRLmo7cUV2vxnvRnMbN+wOPAN9x9f1Lic/dadz+X6OziAjM7Owmxmdmngd3uvqKtunHHluJj7j4JmAncaGafTEh8eURDz/e5+3nAIaIhoiTEFjU2yweuAH7XVtW4YgvXbmYRDZsNB/qa2dXZjk3f42lBSUmJl5aWZjsMEZEuZcWKFU50XajF5KJbX7egtLSU8vLybIchItKlmNne1pIOaKhNREQ619a2KuiMJ0YPvbKl2fIvTB4dcyQiIhlzvK0KOuMREZFYKfGIiEislHhERCRWSjwiIhIrJR4REYmVEo+IiMRKiUdERGKlxCMiIrFS4hERkVgp8YiISKyUeEREJFZKPCIiEislHhERiZUSj4iIxEq3RUgw3UZBRLojnfGIiEisdMbTjegMSUS6AiWeBGgpYYiIdEcaahMRkVgp8YiISKyUeEREJFZKPCIiEitNLujhNBNOROKmMx4REYlVYhOPmT1oZrvNbFVKWZGZLTWzDeF5cMq+28yswszWm9llKeXnm9nKsO8eM7O4P4uIiHwgsYkH+BUwo1HZXOBZd58APBteY2YTgdnAWaHNf5hZbmhzH3A9MCE8Gh9TRERilNjE4+7PA+81Kp4FzA/b84HPpJQ/4u7H3H0jUAFcYGbDgAHu/pK7O7AgpY2IiGRBV5tcMNTddwC4+w4zOyWUjwBeTqm3NZRVh+3G5V2aVjoQka4ssWc87dTcdRtvpbz5g5hdb2blZlZeWVnZacGJiMgHulri2RWGzwjPu0P5VmBUSr2RwPZQPrKZ8ma5+zx3L3P3siFDhnRq4CIiEulqiWchMCdszwGeSCmfbWYFZjaWaBLB8jAsd8DMpoTZbNektBERkSxI7DUeM3sYmAqUmNlW4HvA94HHzOxaYAvweQB3X21mjwFrgBrgRnevDYf6GtEMud7A4vAQEZEsSWzicfcrW9j1qRbq3w3c3Ux5OXB2J4YmIiInoasNtYmISBeX2DMe6TwdmX6tNdxEJFN0xiMiIrFS4hERkVgp8YiISKyUeEREJFZKPCIiEislHhERiZUSj4iIxEqJR0REYqXEIyIisVLiERGRWCnxiIhIrJR4REQkVko8IiISK61OnQEdWQ1aRKSn0BmPiIjESolHRERipaE2aRfdIE5ETpbOeEREJFZKPCIiEislHhERiZUSj4iIxEqJR0REYtVjZrWZ2Qzgp0Au8IC7fz/LIXUrmu0mIunqEYnHzHKBnwHTga3Aq2a20N3XZDey7k8JSUQa6xGJB7gAqHD3dwDM7BFgFqDEkyXtXVaopUTVWccRkfj0lMQzAng35fVWYHLjSmZ2PXB9eHnQzNa3cswSYE+nRdi5ul1sV3XSm7dxnCT3GyQ7PsXWMd0xtjFtVegpiceaKfMmBe7zgHlpHdCs3N3LTjawTFBsHZPk2CDZ8Sm2jumpsfWUWW1bgVEpr0cC27MUi4hIj9ZTEs+rwAQzG2tm+cBsYGGWYxIR6ZF6xFCbu9eY2deBp4mmUz/o7qtP8rBpDclliWLrmCTHBsmOT7F1TI+MzdybXOoQERHJmJ4y1CYiIgmhxCMiIrFS4mknM5thZuvNrMLM5mbwfR40s91mtiqlrMjMlprZhvA8OGXfbSGm9WZ2WUr5+Wa2Muy7x8wslBeY2aOh/BUzK21HbKPM7DkzW2tmq83slqTEZ2aFZrbczN4Isd2ZlNhSjptrZn8zs6cSGNumcNzXzaw8SfGZ2SAz+72ZrQv/9i5MQmxm9qHQX/WP/Wb2jSTEFtp+M/xfWGVmD1v0fyS7sbm7Hmk+iCYmvA2MA/KBN4CJGXqvTwKTgFUpZT8E5obtucAPwvbEEEsBMDbEmBv2LQcuJPou02JgZii/Abg/bM8GHm1HbMOASWG7P/BWiCHr8YXj9AvbvYBXgClJiC0lxluBh4CnkvRzDW02ASWNyhIRHzAf+ErYzgcGJSW2Rr8jdhJ9iTLrsRF9eX4j0Du8fgz4YrZjy/ov8670CJ3+dMrr24DbMvh+pZyYeNYDw8L2MGB9c3EQzd67MNRZl1J+JfDz1DphO4/oG8rWwTifIFoHL1HxAX2A14hWqUhEbETfIXsWuIQPEk8iYgttNtE08WQ9PmAA0S9QS1psjeK5FHgxKbHxwaotRaHdUyHGrMamobb2aW7pnRExvv9Qd98BEJ5PaSOuEWG7cfkJbdy9BtgHFLc3oHBafR7RmUUi4gtDWa8Du4Gl7p6Y2ICfAN8C6lLKkhIbRCt6PGNmKyxaQiop8Y0DKoFfhmHKB8ysb0JiSzUbeDhsZz02d98G/AjYAuwA9rn7M9mOTYmnfdJaeicLWoqrtXhP+rOYWT/gceAb7r4/KfG5e627n0t0dnGBmZ2dhNjM7NPAbndf0VbduGNL8TF3nwTMBG40s08mJL48oqHn+9z9POAQ0RBREmKLGkdfTr8C+F1bVeOKLVy7mUU0bDYc6GtmV2c7NiWe9sn20ju7zGwYQHje3UZcW8N24/IT2phZHjAQeC/dQMysF1HS+a27/yFp8QG4+17gT8CMhMT2MeAKM9sEPAJcYma/SUhsALj79vC8G/gvopXdkxDfVmBrOHsF+D1RIkpCbPVmAq+5+67wOgmxTQM2unulu1cDfwAuynZsSjztk+2ldxYCc8L2HKJrK/Xls8PskrHABGB5OIU+YGZTwgyUaxq1qT/W54D/9jBI25ZwrP8E1rr7j5MUn5kNMbNBYbs30X+8dUmIzd1vc/eR7l5K9G/nv9396iTEBmBmfc2sf/020bWAVUmIz913Au+a2YdC0aeIbmuS9dhSXMkHw2yNj5et2LYAU8ysTzjmp4C1WY+tPRfO9HCAy4lmcb0NfCeD7/Mw0ZhsNdFfFNcSjZs+C2wIz0Up9b8TYlpPmG0SysuIfnm8Dfw7H6xWUUg0JFBBNFtlXDti+zjRqfSbwOvhcXkS4gM+DPwtxLYK+G4oz3psjeKcygeTCxIRG9F1lDfCY3X9v+8ExXcuUB5+tn8EBicotj5AFTAwpSwpsd1J9MfXKuDXRDPWshqblswREZFYaahNRERipcQjIiKxUuIREZFYKfGIiEislHhERCRWSjwiCWBmtRatbLzKzH5nZn1aqPfXuGMT6WxKPCLJcMTdz3X3s4HjwFdTd5pZLoC7X5SN4EQ6kxKPSPK8AIw3s6kW3ffoIWAlgJkdrK9kZt8K90d5w8y+H8pOM7MlYZHPF8zsjOx8BJGW5WU7ABH5QFjraiawJBRdAJzt7hsb1ZsJfAaY7O6Hzawo7JoHfNXdN5jZZOA/iG7BIJIYSjwiydA73MoBojOe/yRazHF546QTTAN+6e6HAdz9vbBa+EXA76LltIBoeRSRRFHiEUmGIx7dyqFBSB6HWqhvNF16PgfY2/g4IkmjazwiXdMzwJfrZ7+ZWZFH90TaaGafD2VmZh/JZpAizVHiEemC3H0J0XL05WGI7l/CrquAa82sfoXpWdmJUKRlWp1aRERipTMeERGJlRKPiIjESolHRERipcQjIiKxUuIREZFYKfGIiEislHhERCRW/x9Q9kMR6O7ECQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot(data,\"Price\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "3108ae45",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Price']=np.where(data['Price']>=35000,data['Price'].median(),data['Price'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b29ce6c3",
   "metadata": {},
   "source": [
    "shreyas is here for the reason"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "fea62f8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>0</td>\n",
       "      <td>3897.0</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2</td>\n",
       "      <td>7662.0</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>4</td>\n",
       "      <td>19h 0m</td>\n",
       "      <td>2</td>\n",
       "      <td>13882.0</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>3</td>\n",
       "      <td>5h 25m</td>\n",
       "      <td>1</td>\n",
       "      <td>6218.0</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>2</td>\n",
       "      <td>4h 45m</td>\n",
       "      <td>1</td>\n",
       "      <td>13302.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline    Source  Destination Duration  Total_Stops    Price  Joruney_day  \\\n",
       "0        3  Banglore            2   2h 50m            0   3897.0           24   \n",
       "1        7   Kolkata            3   7h 25m            2   7662.0            5   \n",
       "2       10     Delhi            4   19h 0m            2  13882.0            6   \n",
       "3        3   Kolkata            3   5h 25m            1   6218.0            5   \n",
       "4        3  Banglore            2   4h 45m            1  13302.0            3   \n",
       "\n",
       "   Joruney_month  Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  \\\n",
       "0              3             22               20                  1   \n",
       "1              1              5               50                 13   \n",
       "2              9              9               25                  4   \n",
       "3             12             18                5                 23   \n",
       "4              1             16               50                 21   \n",
       "\n",
       "   Arrival_Time_minute  SourceBanglore  SourceKolkata  SourceDelhi  \\\n",
       "0                   10               1              0            0   \n",
       "1                   15               0              1            0   \n",
       "2                   25               0              0            1   \n",
       "3                   30               0              1            0   \n",
       "4                   35               1              0            0   \n",
       "\n",
       "   SourceChennai  SourceMumbai  \n",
       "0              0             0  \n",
       "1              0             0  \n",
       "2              0             0  \n",
       "3              0             0  \n",
       "4              0             0  "
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "ddf9cead",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.drop(columns=['Source','Duration'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "13567b6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>3897.0</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>7662.0</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline  Destination  Total_Stops   Price  Joruney_day  Joruney_month  \\\n",
       "0        3            2            0  3897.0           24              3   \n",
       "1        7            3            2  7662.0            5              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \\\n",
       "0             22               20                  1                   10   \n",
       "1              5               50                 13                   15   \n",
       "\n",
       "   SourceBanglore  SourceKolkata  SourceDelhi  SourceChennai  SourceMumbai  \n",
       "0               1              0            0              0             0  \n",
       "1               0              1            0              0             0  "
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "f4084506",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Airline                  int64\n",
       "Destination              int64\n",
       "Total_Stops              int64\n",
       "Price                  float64\n",
       "Joruney_day              int64\n",
       "Joruney_month            int64\n",
       "Dep_Time_hour            int64\n",
       "Dep_Time_minute          int64\n",
       "Arrival_Time_hour        int64\n",
       "Arrival_Time_minute      int64\n",
       "SourceBanglore           int64\n",
       "SourceKolkata            int64\n",
       "SourceDelhi              int64\n",
       "SourceChennai            int64\n",
       "SourceMumbai             int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "727ba4e8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "f72886f7",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'mutual_info_regressiont' from 'sklearn.feature_selection' (C:\\Users\\Shreyas\\anaconda3\\lib\\site-packages\\sklearn\\feature_selection\\__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-93-b357b0a3aa2d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfeature_selection\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mmutual_info_regressiont\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m: cannot import name 'mutual_info_regressiont' from 'sklearn.feature_selection' (C:\\Users\\Shreyas\\anaconda3\\lib\\site-packages\\sklearn\\feature_selection\\__init__.py)"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_selection import mutual_info_regressiont"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "febb6131",
   "metadata": {},
   "outputs": [],
   "source": [
    "#conda install mutual_info_regressiona"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7f858d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_selection import mutual_info_regressions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0de26d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "bda2873b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_selection import mutual_info_regression\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "4fd2e336",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=data.drop(['Price'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "9c1954f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "y=data['Price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "6f0ce655",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.97788657, 1.00120655, 0.79178823, 0.18735737, 0.24343235,\n",
       "       0.32624237, 0.25243238, 0.39994579, 0.34022108, 0.37943519,\n",
       "       0.46036547, 0.52011948, 0.13904019, 0.19808989])"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mutual_info_regression(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "7ef0d88a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Price</th>\n",
       "      <th>Joruney_day</th>\n",
       "      <th>Joruney_month</th>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <th>SourceBanglore</th>\n",
       "      <th>SourceKolkata</th>\n",
       "      <th>SourceDelhi</th>\n",
       "      <th>SourceChennai</th>\n",
       "      <th>SourceMumbai</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>3897.0</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>7662.0</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>50</td>\n",
       "      <td>13</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>13882.0</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>25</td>\n",
       "      <td>4</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>6218.0</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>18</td>\n",
       "      <td>5</td>\n",
       "      <td>23</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>13302.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>50</td>\n",
       "      <td>21</td>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Airline  Destination  Total_Stops    Price  Joruney_day  Joruney_month  \\\n",
       "0        3            2            0   3897.0           24              3   \n",
       "1        7            3            2   7662.0            5              1   \n",
       "2       10            4            2  13882.0            6              9   \n",
       "3        3            3            1   6218.0            5             12   \n",
       "4        3            2            1  13302.0            3              1   \n",
       "\n",
       "   Dep_Time_hour  Dep_Time_minute  Arrival_Time_hour  Arrival_Time_minute  \\\n",
       "0             22               20                  1                   10   \n",
       "1              5               50                 13                   15   \n",
       "2              9               25                  4                   25   \n",
       "3             18                5                 23                   30   \n",
       "4             16               50                 21                   35   \n",
       "\n",
       "   SourceBanglore  SourceKolkata  SourceDelhi  SourceChennai  SourceMumbai  \n",
       "0               1              0            0              0             0  \n",
       "1               0              1            0              0             0  \n",
       "2               0              0            1              0             0  \n",
       "3               0              1            0              0             0  \n",
       "4               1              0            0              0             0  "
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "1333dfbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "imp=pd.DataFrame(mutual_info_regression(x,y),index=x.columns)\n",
    "imp.columns=['importance']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "9ffed3a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>importance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Destination</th>\n",
       "      <td>1.003552</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Airline</th>\n",
       "      <td>0.980647</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Total_Stops</th>\n",
       "      <td>0.783683</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceDelhi</th>\n",
       "      <td>0.516092</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceKolkata</th>\n",
       "      <td>0.455894</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <td>0.407193</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceBanglore</th>\n",
       "      <td>0.392736</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <td>0.353136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <td>0.338687</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <td>0.261859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Joruney_month</th>\n",
       "      <td>0.238920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceMumbai</th>\n",
       "      <td>0.199985</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Joruney_day</th>\n",
       "      <td>0.189863</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceChennai</th>\n",
       "      <td>0.137181</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     importance\n",
       "Destination            1.003552\n",
       "Airline                0.980647\n",
       "Total_Stops            0.783683\n",
       "SourceDelhi            0.516092\n",
       "SourceKolkata          0.455894\n",
       "Arrival_Time_hour      0.407193\n",
       "SourceBanglore         0.392736\n",
       "Arrival_Time_minute    0.353136\n",
       "Dep_Time_hour          0.338687\n",
       "Dep_Time_minute        0.261859\n",
       "Joruney_month          0.238920\n",
       "SourceMumbai           0.199985\n",
       "Joruney_day            0.189863\n",
       "SourceChennai          0.137181"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imp.sort_values(by='importance',ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "5852bcb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>importance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Airline</th>\n",
       "      <td>0.980647</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Destination</th>\n",
       "      <td>1.003552</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Total_Stops</th>\n",
       "      <td>0.783683</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Joruney_day</th>\n",
       "      <td>0.189863</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Joruney_month</th>\n",
       "      <td>0.238920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dep_Time_hour</th>\n",
       "      <td>0.338687</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dep_Time_minute</th>\n",
       "      <td>0.261859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Arrival_Time_hour</th>\n",
       "      <td>0.407193</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Arrival_Time_minute</th>\n",
       "      <td>0.353136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceBanglore</th>\n",
       "      <td>0.392736</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceKolkata</th>\n",
       "      <td>0.455894</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceDelhi</th>\n",
       "      <td>0.516092</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceChennai</th>\n",
       "      <td>0.137181</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SourceMumbai</th>\n",
       "      <td>0.199985</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     importance\n",
       "Airline                0.980647\n",
       "Destination            1.003552\n",
       "Total_Stops            0.783683\n",
       "Joruney_day            0.189863\n",
       "Joruney_month          0.238920\n",
       "Dep_Time_hour          0.338687\n",
       "Dep_Time_minute        0.261859\n",
       "Arrival_Time_hour      0.407193\n",
       "Arrival_Time_minute    0.353136\n",
       "SourceBanglore         0.392736\n",
       "SourceKolkata          0.455894\n",
       "SourceDelhi            0.516092\n",
       "SourceChennai          0.137181\n",
       "SourceMumbai           0.199985"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "imp"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76a90dc2",
   "metadata": {},
   "source": [
    "BUILDING ML MODEL...\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7801549c",
   "metadata": {},
   "source": [
    "hyperparameters "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59637000",
   "metadata": {},
   "source": [
    "to build the ml model we need randam data an testing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "87ef4de5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "6a87bf6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#   train_test_split()\n",
    "#shift tab to gte the above details "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "b7e02847",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "f32608d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "11941632",
   "metadata": {},
   "outputs": [],
   "source": [
    "ml_model=RandomForestRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "d56da1e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=ml_model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "981ba631",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=model.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "754a8e2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([16677.04  ,  6319.66  ,  9049.75  , ...,  8405.05  ,  8779.07  ,\n",
       "       11745.6015])"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "cd555e0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3526"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(x_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e16c16b8",
   "metadata": {},
   "source": [
    "built the ml model "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fad5f693",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46e8c072",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "d2c75c73",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: Could not find a version that satisfies the requirement pickle\n",
      "ERROR: No matching distribution found for pickle\n"
     ]
    }
   ],
   "source": [
    "!pip install pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67c1c126",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "38709888",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "d95d5334",
   "metadata": {},
   "outputs": [],
   "source": [
    "file=open(r'D:\\ml_model/rf_random.pkl','wb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "b1e1f26e",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(model,file)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f948edb",
   "metadata": {},
   "source": [
    "this stores the co-efficient of the ML model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "f16f42f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=open(r'D:\\ml_model/rf_random.pkl','rb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "d028a4ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "forest=pickle.load(model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "5a6b8f53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([16677.04  ,  6319.66  ,  9049.75  , ...,  8405.05  ,  8779.07  ,\n",
       "       11745.6015])"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forest.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36cdca88",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "287bddcf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a83f0439",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b183bae6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
