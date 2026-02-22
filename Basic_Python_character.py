{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60472a8b-4dc1-4dd9-b831-c2603e270529",
   "metadata": {},
   "outputs": [],
   "source": [
    "full_dot = '●'\n",
    "empty_dot = '○'\n",
    "\n",
    "def create_character(name,strength,intelligence,charisma):{\n",
    "\"\"\"The function assign the name and stats of a character\"\"\"\n",
    "\n",
    "#Name validation\n",
    "    if isinstance(name,str)==False: print(\"The character name should be a string\"\n",
    "    if name.strip()==\"\": print(\"The character should have a name\")\n",
    "    if len(name.strip())>10: print(\"The character name is too long\")\n",
    "    if len(name.split())>1: print(\"The character name should not contain spaces\")\n",
    "#Stats validation\n",
    "stats=(strength,intelligence,charisma)\n",
    "    if len(isinstance(stats,int))<3: print(\"All stats should be integers\")\n",
    "    if \n",
    "\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5b5fb8ae-19d0-4e31-9dde-2b63a7206dad",
   "metadata": {},
   "outputs": [],
   "source": [
    "name=\"ciccio\"\n",
    "stats=[1,2,3]\n",
    "strength=1\n",
    "intelligence=2\n",
    "charisma=3\n",
    "for i in stats:\n",
    "    if isinstance(i,int)==False: \n",
    "        print(\"cacca\")\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6313f811-464a-4162-87ea-43368ccbcc11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All stats should be integers\n"
     ]
    }
   ],
   "source": [
    "for i in stats: \n",
    "    if isinstance(i,int)==False: print(\"All stats should be integers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "189c7e97-31a1-484d-aac9-1d4675e64cd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(stats)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e51e03d7-38cd-4692-b007-5ac642319452",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ciccio\n",
      "STR ●○○○○○○○○○\n",
      "INT ●●○○○○○○○○\n",
      "CHA ●●●○○○○○○○\n"
     ]
    }
   ],
   "source": [
    "full_dot = '●'\n",
    "empty_dot = '○'\n",
    "\n",
    "print(name,\"\\n\",\"STR \",full_dot*strength,empty_dot*(10-strength),\"\\n\",\"INT \",full_dot*intelligence,empty_dot*(10-intelligence),\"\\n\",\"CHA \",full_dot*charisma,empty_dot*(10-charisma),sep=\"\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
