import { Module } from '@nestjs/common';
import { RestaurantModule } from './restaurants/restaurant.module';
import { CustomersModule } from './customers/customers.module';

@Module({
  imports: [RestaurantModule, CustomersModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
