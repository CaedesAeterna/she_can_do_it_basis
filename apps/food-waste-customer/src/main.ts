import { NestFactory } from '@nestjs/core';
import { UserModule } from './user.module';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

async function bootstrap() {
  const app = await NestFactory.create(UserModule);

  const config = new DocumentBuilder()
    .setTitle('Food Waste Customer')
    .setDescription('The Customer App API description')
    .setVersion('1.0')
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  await app.listen(process.env.port ?? 3000);
}
bootstrap();