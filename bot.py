B
    5�]-  �            	   @   s8  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZm	Z	m
Z
 d dlmZ d dlmZ ejdd� ejdd�Zejd	d
d dd� e�� Zedd��Ze�� ZW dQ R X e�e�Zee
jej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j ej! d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d e
j  d  e
j ej d! e
j  d" � e
jej Z"e
j Z#e
jej Z$e
jej Z%e
jej Z&e
jej! Z'e
jej! Z(e �)� Z*d#Z+d$d%d&d'd(d)d*�Z,d+d,� Z-d-d.� Z.d/d0� Z/e*j0e+e,d1d2ed3 d4 ed3 d5 d6d7�d8�Z1e�e1j2�Z3y4ee"d9 e$ d e# e4e5e3d: d; �d< � � W n   ed=� e�6�  Y nX e/e7e5ed> �d< �e7e5ed? �d< �� dS )@�    N)�Fore�Back�Style)�randint)�datetimeT)Z	autoresetz&Script Untuk Menuyul Website CowDollar)�descriptionz-cz--betsetz%Enter Your Betset Number (default: 0))�default�helpzconfig.json�rz�      ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/z)
=======================================
zAuthor By  z: zKadal15
zChannel Yt �:z Jejaka Tutorialz
999 Dice Botz | zLose Streak �|z Win Streak
zDonate z BTC z#18961sqv9fPuBcEbbi1gHub8ydWePB8yaG
z         LTC z#LNRkk6o9h1Rh98sDW8byeH9HbeUHwNohDu
z         Doge z$DJG4YG3ARUkSt9e5xvHvSS3faVx3v1HM9p

z$https://www.999doge.com/api/web.aspxzfile://z�Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36z!application/x-www-form-urlencodedz*/*z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7zcom.reland.relandicebot)ZOriginz
user-agentzContent-typeZAcceptzAccept-LanguagezX-Requested-Withc             C   s�   t dt| � d �}|dks,|dks,|dkrbt |�d�d �}dt|� }tt|�d	|  �ada|d
ks�|dks�|dks�|dks�|dkr�dat|�d�d �ad S )Ni?B �d   �Hi�hiZHI�.�   �   �
   �LoZLOW�low�LowZLOr   )�str�float�split�len�intr   �high)ZpersenZtaruhan�c�nZpangkat� r   �dice.py�konvert3   s    (r!   c             C   s�   t | �dk r4tdt | � �}|d t| � } d|  }t | �dkrjtdt | � �}|d t| � } d|  }n0t | �}| dd � }| d |d � }|d | }|S )N�   �0z0.i����r   )r   r   r   )�numZpanjang_nol�resultZlen_num�end�firstr   r   r    �revA   s    
r(   c          	   C   sV  t jdkst jdkst jdkrZd}d}x<|d7 }ytd | d }W q(   P Y q(X q(W n
tt j�}ttd | d �d	 }ttd | d
 �d }tttd | d �d �}ttd | d td | d d � |}dtd |ttt	dd�ddd�}	�
y.t
jtt|	d�}
t�|
j�}|d t|d � t|� }t|d �t|� }t|d t|d � t|� | �d }ttd tttt|d �t|� �d � � tdtd | d  � d}d}d}d}t�� �d�}t|�ttd � }d}d}d}d}d}d}�	x"td | d dk�sHtd | d dk�sHtd | d d k�rVtj�d!� n&|tttd | d �d �k�r||}td | d d" d# d$k�s�td | d d" d# d%k�s�td | d d" d# d&k�r�|d7 }|d'k�rD|ttd | d d" d( �d k�rd)}|ttd | d d" d( �d* d k�rDd}d}|d'k�r�|ttd | d d" d+ �d k�rxd)}|ttd | d d" d+ �d* d k�r�d}d}ntd | d d }t jdk�s�t jdk�s�t jdk�r�t�� �d�}t|�t|d �k�r�t|�ttd � }|d7 }||k�r2d}td,td | d  d- � ttd | d �d	 }ttd | d
 �d }tttd | d �d �}n
tt j�}td | d. d# d%k�s�td | d. d# d$k�s�td | d. d# d&k�r�tt�ttd | d. d/ �ttd | d. d0 ��d*�}tt|��}|d1k�r\tj�d2t|� d3 � |d4k�r~tj�d2t|� d5 � |d6k�r�tj�d2t|� d7 � t|t|�� nttd | d t|�� t� t|�� t|�}|d7 }dtd |ttt	dd�ddd�}	|ttd8 �k�r�ttd9 t d: t t|� � t!�"d;t|� � t� d� t!�"d<ttt|d �t|� �d � � t�#�  t
jtt|	d�}
t�|
j�}t|d t|d � t|� | �d }t|d �t|� }|d | k�r�tt$d= t t|� t$ d> t% tt|�d � tttt|d �t|� �d � t%d? tt|� � ttd@ � t!�"dA� t� d� t!�"d<ttt|d �t|� �d � � t�#�  |d |k �rxtt$d= t t|� t$ dB t& dC tt|�d � tttt|d �t|� �d � t&dD tt|� � tt'j(t)j* dE � t!�"dF� t� d� t!�"d<ttt|d �t|� �d � � t�#�  |d dk	�	r`|d7 }d}t|d �t|� }|dk�	rtt$d= t t|� t$ d> t% tt+t|��� ttt+t|��� t%d? tt|� � nVtt$d= t t|� t$ d> t% tt+t|��� ttt+t|��� t&dD tt|� � n�d}|d7 }d}d'}t|d �t|� }|dk�	r�tt$d= t t|� t$ dB t& dC tt+t|��� ttt+t|��� t%d? tt|� � nZtt$d= t t|� t$ dB t& dC tt+t|��� ttt+t|��� t&dD tt|� � |d'k�
r�|d7 }t|�ttd | d+ � }||k�
r�d}d}n0||k�
r�d}|}nt|�ttd | d( � }||k�
r�d'}d}|d7 }||k�
r�d'}d}|d7 }tj�tdG t t|� t, dH t t|� d2 � �qW W n&   td!� t!�"dI� t�#�  Y nX d S )JNZAuto�autoZAUTOr   r   ZConfigzName Bet SetZIntervali�  zReset If WinzBase Beti ��ZChanceZBetZPlaceBetZSessionCookiei?B Zdoge�2)�a�sZPayInr   ZHighZ
ClientSeedZCurrencyZProtocolVersion)�headers�dataZStartingBalanceZPayOutz


Starting BalancezAnda Menggunakan BetSet Ke Fz%Mr   zMax BetZOFFZoffZOff� zHi / LowZToggleZOnZON�onTzIf Winr   �   zIf LosezChange Bet Set z                           zRandom ChanceZMinZMax�   �z   �   z  �   � zTarget Profitz$Yay.! 
Profit Mencapai Target.....!
zProfit ztermux-toast You win ztermux-toast Total Balance �[z] ZProfitz)Yay.!
Balance Sudah Memenuhi Target.....!z&termux-toast Target Win Sudah Tercapai�]�-zLose zLose Target....!ztermux-toast Lose Target zWin Streak z Lose Streak ztermux-toast Betting Stop)-�my_namespaceZbetset�objr   r   r!   �jsr   r   r   r   Zpost�url�ua�json�loads�text�print�hijau�resr   r   �now�strftime�sys�stdout�write�round�random�uniformr   �time�sleep�os�system�exit�ungu�hijau2�red2r   �BRIGHTr   �REDr(   �red)ZwsZlsZurutZjumlahulangZpesanZslpZlimit_aZpayinZamountr.   Zr1ZjsnZjumblZjumZprofr   ZburstZstats_rolebet_loseZstats_rolebet_winZmenitZno_winZno_loseZ	total_winZ
total_loseZ
no_rolebetZrolebetZwaktuZhasil_chanceZcokZbal�ir   r   r    �diceR   s>   
&(.B"Z
&*
&*$

N:


 
*(f

*j

*
XX
\Z




>
rY   ZLoginZ 7ec7f8a2c9724b2cbb8ed75e72b47ee9ZAccount�Username�Passwordr/   )r+   ZKeyrZ   r[   ZTotp)r-   r.   zBalance ZDogeZBalancei ��z%Check Your Username And Your Passwordz
Target WinzLose Target)8Zrequestsr?   rM   rG   rK   rO   �argparseZcoloramar   r   r   r   r   �init�ArgumentParser�parser�add_argument�
parse_argsr:   �openZmyfile�readr.   r@   r;   rB   ZNORMALZMAGENTAZGREENrU   ZDIMZWHITEZ	RESET_ALLrV   rC   rD   Zabu2rR   rS   rT   rW   Zsessionr   r=   r>   r!   r(   rY   �getr
   rA   r<   r   r   rQ   r   r   r   r   r    �<module>   sV   8
� 7 8,4