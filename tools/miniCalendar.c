#include <stdio.h>
#include <stdbool.h>








bool isLeapYear(int year)
{
  return !(year%4) && (year%100 || !(year%400));
}


void add_days_to_date(int* mm, int* dd, int* yyyy, int days_left_to_add)
{
  /*
    Thirty days hath September, 
    April, June, and November,
    All the rest have thirty-one, 
    Excepting February alone,
    And that has twenty-eight days clear, 
    And twenty-nine in each leap year.
  */
  // define number of days in the year (regular and leap)
  int yearsDays[][12] = 
  {
    { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }, 
    { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }
  };


  // loop through days to add
  for(days_left_to_add; 0<days_left_to_add; --days_left_to_add)
  {
    if(++*dd > yearsDays[isLeapYear(*yyyy)][*mm -1])
    {
      *dd = 1;
      ++*mm;
    }
    if(*mm > 12)
    {
      *mm = 1;
      ++*yyyy;
    }
  }
}

void outputDate(int* mm, int* dd, int* yyyy)
{
  switch(*mm) 
  {
    case 1:
      printf("January ");
      break;
    case 2:
      printf("February ");
      break;
    case 3:
      printf("March ");
      break;
    case 4:
      printf("April ");
      break;
    case 5:
      printf("May ");
      break;
    case 6:
      printf("June ");
      break;
    case 7:
      printf("July ");
      break;
    case 8:
      printf("August ");
      break;
    case 9:
      printf("September ");
      break;
    case 10:
      printf("October ");
      break;
    case 11:
      printf("November ");
      break;
    case 12:
      printf("December ");
      break;
  }
  switch(*dd)
  {
    case 1: case 21: case 31:
      printf("%dst, ", *dd);
      break;
    case 2: case 22:
      printf("%dnd, ", *dd);
      break;
    case 3: case 23:
      printf("%drd, ", *dd);
      break;
    default:
      printf("%dth, ", *dd);
  }
  printf("%d\n", *yyyy);
}


int main()
{
  int todayMonth = 1;
  int todayDays = 4;
  int todayYear = 2022;
  
  int outputMonth = todayMonth;
  int outputDays = todayDays;
  int outputYear = todayYear;
  
  printf("was: ");
  outputDate(&outputMonth, &outputDays, &outputYear);
  add_days_to_date(&outputMonth, &outputDays, &outputYear, 7000);
  printf("now: ");
  outputDate(&outputMonth, &outputDays, &outputYear);
  printf("today: ");
  outputDate(&todayMonth, &todayDays, &todayYear);
}







