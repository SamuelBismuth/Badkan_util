using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IgIgul
{
    class Program
    {
        static void Main(string[] args)
        {
            int torot = 1, hator, xtor, ytor;
            int i, j;

            char[,] arr = new char[,]
            //{
            //    {'-','-','-'},
            //    {'-','-','-'},
            //    {'-','-','-'}
            //};

            // use this for automated input
            {
                { 'O','X','X'},
                { 'X','X','O'},
                { 'O','O','X'}
            };

            //for (torot = 1; torot <= 9; torot++)
            //{
            //    hator = torot % 2;
            //    if (hator == 0) hator = 2;
            //    Console.WriteLine("Now it is the turn of player {0}.\n", hator);
            //    Console.WriteLine("what is your x coordionate 0-1-2 ?");
            //    xtor = int.Parse(Console.ReadLine());
            //    Console.WriteLine("what is your ycoordionate 0-1-2 ?");
            //    ytor = int.Parse(Console.ReadLine());
            //    if (arr[xtor,ytor] != '-')
            //    {
            //        Console.WriteLine("\n\n\n*****************\nTHIS IS TAKEN. Leaving.....");
            //        throw new Exception();
            //    }
            //    if (hator == 1) arr[xtor,ytor] = 'X';
            //    else arr[xtor,ytor] = 'O';
            //    printluach(arr);
            //}

            printluach(arr);
            bdika(arr);
            Console.ReadLine();
       

        void printluach(char[,] tavla)
        {
                for (i = 0; i <= 2; i++)
                {
                    for (j = 0; j <= 2; j++)
                        Console.Write("{0}  ", tavla[i, j]); //(" % 4c", tavla[i][j]);
                    Console.WriteLine();
                    Console.WriteLine();
                }
            //        foreach (int q in tavla)
            //        Console.Write("{0}  ", tavla[i, j]); //(" % 4c", tavla[i][j]);
        }


        int checkrow(char[,] tavla, int r)
        {

            if (tavla[r,0] == tavla[r,1] && (tavla[r,1] == tavla[r,2]))
            {
                if (tavla[r,0] == 'X') return 1;
                else return 2;
            }
            return 0;
        }


        int checkcol(char[,] tavla, int r)
        {

            if (tavla[0,r] == tavla[1,r] && (tavla[1,r] == tavla[2,r]))
            {
                if (tavla[r,0] == 'X') return 1;
                else return 2;
            }
            return 0;
        }




            void bdika(char[,] tavla)
            {
                if (
                    (checkrow(tavla, 0) == 1) ||
                    (checkrow(tavla, 1) == 1) ||
                    (checkrow(tavla, 2) == 1) ||
                    (checkcol(tavla, 0) == 1) ||
                    (checkcol(tavla, 1) == 1) ||
                    (checkcol(tavla, 2) == 1)
                    )
                    Console.WriteLine("\n Player 1 wins");
                else if (
                    (checkrow(tavla, 0) == 2) ||
                    (checkrow(tavla, 1) == 2) ||
                    (checkrow(tavla, 2) == 2) ||
                    (checkcol(tavla, 0) == 2) ||
                    (checkcol(tavla, 1) == 2) ||
                    (checkcol(tavla, 2) == 2)
                    )
                    Console.WriteLine("\n Player 2 wins");
                else
                    Console.WriteLine("\n Teko");
            }

        } // end of main

    } // end of class program
} // end of namespace
